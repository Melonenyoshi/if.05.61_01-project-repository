public class RomanNumberConverter {
    public static String toRoman(int arabicNumber)
    {
        var romanNumber = "";
        for(var numeral: Numeral.values())
        {
            while(arabicNumber >= numeral.arabic)
            {
                romanNumber += numeral.roman;
                arabicNumber -= numeral.arabic;
            }
        }
        return romanNumber;
    }

    public static int toArabic(String romanNumber) {
        int arabicNumber = 0;
        int lastDigit = 0;
        for(int i = romanNumber.length()-1;i>=0;i--)
        {
            int thisdigit = 0;
            for(var numeral: Numeral.values())
            {
                if(numeral.roman.equals(String.valueOf(romanNumber.charAt(i))))
                {
                    thisdigit = numeral.arabic;
                }
            }

            if(thisdigit >= lastDigit)
            {
                arabicNumber += thisdigit;
            }
            else
            {
                arabicNumber -= thisdigit;
            }
            lastDigit = thisdigit;
        }
        return arabicNumber;
    }

    enum Numeral{
        TEN(10, "X"),
        NINE(9, "IX"),
        FIVE(5, "V"),
        FOUR(4,"IV"),
        ONE(1,"I");
        private final int arabic;
        private final String roman;

        Numeral(int arabic, String roman) {
            this.arabic = arabic;
            this.roman = roman;
        }
    }
}
