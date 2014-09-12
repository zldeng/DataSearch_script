#encoding=utf-8
import sys
import re


def strQ2B(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:
            inside_code = 32  
        elif (inside_code >= 65281 and inside_code <= 65374):
            inside_code -= 65248

        rstring += unichr(inside_code)
    
    return rstring

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

def is_contain_ch(str):
    for ch in str:
        if is_chinese(ch) : return True
    return False

def is_alphabet(uchar):
    if (uchar >= u'\u0041' and uchar<=u'\u005a') \
            or (uchar >= u'\u0061' and uchar<=u'\u007a'):
                return True
    else:
        return False
def is_contain_al(str):
    for ch in str:
        if is_alphabet(ch):
            return True
    
    return False

def isService(subStr):
    subStr = subStr.strip().decode('utf-8')
    if len(subStr) == 0:
        return False
    if subStr[0] == u'(':
        subStr = subStr[1:]
    
    if len(subStr) == 0:
        return False

    if subStr[-1] == u')':
        subStr = subStr[:-1]

    if len(subStr) == 0:
        return False

    subStr = subStr.encode('utf-8')
    
    isService = False
    chKeyword = ['免费', '浴室', '停车' ,'包含', '早餐','海景','景观','烟','男性','女性','网络','卫生间',\
            '河景','浴缸','淋浴','带阳台','加床','泊车','设有','含','城市景','山景','空调','湖景','电梯',\
            '无线网','不可退','退款','壁炉','共享','取消','网络','按摩','水疗','温泉','可供','可使用',\
            '厨房','带露台']
    
    enKeyword = ['free','park','incl','no ','breakfast','Exclude','view ','smoking',\
            'bath','wifi','female','male','access','internet','shower','balcony',\
            'wc','spa','lift','elevator','sea view','only girls','kitchen','terrace',\
            'beach','free zone','garden view','river view','refundable','shuttle',\
            'moviezone','minibar','toilet','public transport','with sofa','extra bed'\
            ,'air conditioning','extra bed','buffet','non ref']
    for keyword in chKeyword:
        if keyword in subStr:
            isService = True
            break

    if isService:
        return isService
    
    matchCount = 0
    if not isService:
        for keyword in enKeyword:
            if keyword in subStr:
                matchCount += 1

    
    isEn = not is_contain_ch(subStr.decode('utf-8')) and is_contain_al(subStr.decode('utf-8'))
    
    if not isEn:
        return isService

    totalCount = len(subStr.strip().split())
    
    #print str(totalCount) + '\t' + str(matchCount)

    if totalCount == 0 or matchCount*1.0 / totalCount < 0.2:
        return False
    else:
        if matchCount > 0:
            isService = True
        return isService

def replaceDot(str):
    chList = list(str.strip())
    for idx in range(1,len(chList)):
        if chList[idx] != ',':
            continue
        else:
            left = False
            right = False

            for lIdx in range(idx-1,-1,-1):
                if chList[lIdx] == ')' and not left:
                    break
                elif chList[lIdx] == '(':
                    left = True
                    break

            for rIdx in range(idx+1,len(chList)):
                if chList[rIdx] == '(' and not right:
                    break
                elif chList[rIdx] == ')':
                    right = True
                    break

            if left and right:
                chList[idx] = '&&'
    #print ''.join(chList)    
    return ''.join(chList)



def normalizeRoomType(srcStr):
    line = strQ2B(srcStr.strip().decode('utf-8')).encode('utf-8').lower()
    #print srcStr 

    line = line.replace('(',' (')
    line = line.replace(')',') ')
    line,num = re.subn('\s+\(',' (',line)

    roomType = line
    
    dotResult = []
    
    roomType = replaceDot(roomType)
    typeList = roomType.strip().split(',')

    for subIdx in range(len(typeList)):
        #unSubStr = typeList[subIdx].decode('utf-8')
        
        otherList = typeList[subIdx].strip().split(' - ')

        otherResult = []
        for otherIdx in range(len(otherList)):
            unOtherStr = otherList[otherIdx].decode('utf-8')
            
            otherStr = otherList[otherIdx]
            #print 'other:' + otherStr

            #chinese
            if is_contain_ch(unOtherStr) and not is_contain_al(unOtherStr):
                subList = otherStr.strip().split(' ')
            
                resultList = []
                
                for idx in range(len(subList)):
                    #第一个描述只处理括号的内容
                    desc = subList[idx]
                    
                    #print desc
                    if desc.count('(') > 0 and desc.count('(') == desc.count(')'):
                        rIdx = desc.rfind(')')
                        rCount = 1
                        
                        lIdx = rIdx
                        for i in range(rIdx-1,-1,-1):
                            if desc[i] == ')':
                                rCount += 1
                            elif desc[i] == '(':
                                rCount -= 1
                            
                            if rCount == 0:
                                lIdx = i
                                break
                        
                        #print 'rIdx:' + str(rIdx) + '  lIdx:' + str(lIdx)

                        if lIdx < rIdx:
                            subStr = desc[lIdx:rIdx+1]
                        else:
                            subStr = ''
                        
                        #print 'subStr:' + subStr
                        #print 'isS:' + str(isService(subStr))

                        if 0 == subIdx and 0 == otherIdx and idx == 0 and not isService(subStr):
                            resultList.append(desc)

                        else:
                            preStr = ''
                            sufStr = ''
                            result = ''
                            if lIdx > 0:
                                preStr = desc[:lIdx]

                            if rIdx < len(desc) - 1:
                                sufStr = desc[rIdx+1:]
                            
                            #print 'preStr:' + preStr + '\t' + str(isService(preStr))
                            #print 'sufStr:' + sufStr + '\t' + str(isService(sufStr))

                            if 0 == subIdx and 0 == otherIdx and idx == 0  or not isService(preStr):
                                result = preStr

                            if not isService(subStr) and subStr != '':
                                result += subStr

                            if not isService(sufStr):
                                result += sufStr

                            if result != '':
                                resultList.append(result)
                        
                    else:
                        if 0 == subIdx and 0 == otherIdx and idx == 0:
                            resultList.append(desc)
                        elif not isService(desc):
                            resultList.append(desc)
                if len(resultList) > 0:
                    otherResult.append(' '.join(resultList))
            #english
            elif is_contain_al(unOtherStr) and not is_contain_ch(unOtherStr):
                if otherStr.count('(') > 0 and  otherStr.count('(') == otherStr.count(')'):
                    rIdx = otherStr.rfind(')')
                    rCount = 1

                    lIdx = rIdx
                    preStr = ''
                    sufStr = ''
                    subStr = ''
                    result = ''

                    for i in range(rIdx-1,-1,-1):
                        if otherStr[i] == ')':
                            rCount += 1
                        elif otherStr[i] == '(':
                            rCount -= 1

                        if rCount == 0:
                            lIdx = i
                            break

                    if lIdx < rIdx:
                        if lIdx > 0:
                            preStr = otherStr[:lIdx]

                        subStr = otherStr[lIdx:rIdx+1]
                        
                        if rIdx < len(otherStr)-1:
                            sufStr = otherStr[rIdx+1:]
                    
                    #print 'lIdx:' + str(lIdx) + '\trIdx:' + str(rIdx)
                    #print 'pre:' + preStr
                    #print 'sub:' + subStr
                    #print 'suf:' + sufStr

                    if subIdx == 0 and otherIdx == 0:
                        result = preStr
                    
                    if not isService(subStr):
                        result += subStr

                    if not isService(sufStr):
                        result += sufStr

                    if result != '':
                        otherResult.append(result)
                    
                else:
                    if subIdx == 0 and otherIdx == 0:
                        otherResult.append(otherStr)
                    elif not isService(otherStr):
                        otherResult.append(otherStr)
            #mixed
            else:
                tmpList = otherStr.strip().split(' ')
                splitList = []
                tmpStr = tmpList[0]
                    
                isCh = is_contain_ch(tmpStr.decode('utf-8'))
                
                for tmpIdx in range(1,len(tmpList)):
                    candStr = tmpList[tmpIdx]
                    flag = is_contain_ch(candStr.decode('utf-8'))

                    if flag == isCh:
                        tmpStr += ' ' + candStr
                        continue
                    else:
                        if subIdx == 0 and otherIdx == 0 and tmpIdx == 1:
                            splitList.append(tmpStr)
                        elif not isService(tmpStr):
                            splitList.append(tmpStr)

                        tmpStr = candStr 
                        isCh = is_contain_ch(candStr.decode('utf-8'))
                
                #print tmpStr + '\t' + str(isService(tmpStr))
                
                if tmpStr != '' and tmpStr[0] == '(' and tmpStr[-1] == ')' and len(splitList) == 0:
                    pass

                elif tmpStr != '' and  not isService(tmpStr) \
                        or subIdx == 0 and otherIdx == 0 and len(tmpList)==1:
                    splitList.append(tmpStr)

                if len(splitList) > 0:
                    otherResult.append(' '.join(splitList))

        if len(otherResult) > 0:
            dotResult.append(' - '.join(otherResult))
    if len(dotResult) > 0:
        for idx in range(len(dotResult)):
            dotResult[idx] = dotResult[idx].replace('不可吸烟','').replace('no smoking','').replace('no-smoking','').replace('free wifi','')
        
        resultRoomType = ','.join(dotResult).replace('&&',',').strip()
        if len(resultRoomType) > 0:
            if resultRoomType[-1] == '-':
                resultRoomType = resultRoomType[:-1].strip()
    else:
        resultRoomType = 'NULL'
    
    unicodeStr = resultRoomType.decode('utf-8')
    if len(unicodeStr) > 0:
        if unicodeStr[-1] == '与'.decode('utf-8') or unicodeStr[-1] == '和'.decode('utf-8'):
            resultRoomType = unicodeStr[:-1].encode('utf-8').strip()

    return resultRoomType

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'python x.py inFile outFile'
        sys.exit(1)


    inFile = file(sys.argv[1])
    outFile = file(sys.argv[2],'w')

    for line in inFile:
        lineList = line.strip().split('\t')
    
        if len(lineList) != 2:
            continue

        srcStr = lineList[0]
        count = lineList[1]

        resultRoomType = normalizeRoomType(srcStr)

        outFile.write(srcStr + '\t' + resultRoomType + '\t' + count + '\n')
