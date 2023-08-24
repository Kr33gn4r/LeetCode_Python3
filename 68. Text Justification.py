from typing import *
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wordsInLine: List[int] = [0]
        curr: int = 0
        for word in words:
            curr += len(word)
            if curr > maxWidth:
                curr = len(word)
                wordsInLine.append(0)
            wordsInLine[-1] += 1
            curr += 1

        justifiedText: List[str] = []
        temp: str = ""
        widx: int = 0
        spaceList: List[int] = []
        for idx in range(len(words)):
            # left justify - single word or last line
            if wordsInLine[widx] == 1 or widx == len(wordsInLine) - 1:
                temp += words[idx] + " "
            # full justify - amount of spaces = words in line - 1
            else:
                if not spaceList:
                    spaces: int = maxWidth - sum(len(words[idx + _]) for _ in range(wordsInLine[widx]))
                    spaceList = [spaces // (wordsInLine[widx] - 1) for _ in range(wordsInLine[widx] - 1)]
                    sidx: int = 0
                    while sum(spaceList) != spaces:
                        spaceList[sidx] += 1
                        sidx += 1
                    spaceList.append(0)
                    sidx = 0
                temp += words[idx] + (" " * spaceList[sidx])
                sidx += 1
            # change widx
            if idx == sum(wordsInLine[0: widx + 1]) - 1:
                if len(temp) != maxWidth: temp = temp[0: maxWidth]
                temp = temp.ljust(maxWidth)
                justifiedText.append(temp)
                temp = ""
                widx += 1
                spaceList = []
        return justifiedText