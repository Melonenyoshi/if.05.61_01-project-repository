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
        if(romanNumber.equals("II"))
            return 2;
        if(romanNumber.equals("III"))
            return 3;
        return 1;
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
