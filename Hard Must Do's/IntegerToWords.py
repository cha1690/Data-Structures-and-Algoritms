class Solution:
    def intToWords(self,num):
        self.tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.ones = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                     "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        numInWords=""

        if num == 0:
            return "Zero"

        if (num// 1000000000) != 0:
            numInWords += self.intToWords(num// 1000000000) + "Billion"
            num%=1000000000

        if (num// 1000000) != 0:
            numInWords += self.intToWords(num// 1000000) + "Million"
            num%=1000000

        if (num// 1000) != 0:
            numInWords += self.intToWords(num// 1000) + "Thousand"
            num%=1000

        if (num// 100) != 0:
            numInWords += self.intToWords(num// 100) + "Hundred"
            num%=100

        if num >= 20 and (num// 10) != 0:
            numInWords += self.tens[num//10 - 2] + " "
            num%=10

        if num != 0:
            numInWords += self.ones[num - 1] + " "

        return numInWords.strip()