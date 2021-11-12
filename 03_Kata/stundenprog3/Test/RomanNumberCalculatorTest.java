import org.junit.Assert;
import org.junit.Test;

public class RomanNumberCalculatorTest {
    @Test
    public void itShouldReturnI_Given1() {
        Assert.assertEquals("I",RomanNumberConverter.toRoman(1));
    }
    @Test
    public void itShouldReturnII_Given2()
    {
        Assert.assertEquals("II",RomanNumberConverter.toRoman(2));
    }
    @Test
    public void itShouldReturnIII_Given3()
    {
        Assert.assertEquals("III",RomanNumberConverter.toRoman(3));
    }
    @Test
    public void itShouldReturnV_Given5()
    {
        Assert.assertEquals("V",RomanNumberConverter.toRoman(5));
    }
    @Test
    public void itShouldReturnVIs_GivenBetween6And8()
    {
        Assert.assertEquals("VI",RomanNumberConverter.toRoman(6));
        Assert.assertEquals("VII",RomanNumberConverter.toRoman(7));
        Assert.assertEquals("VIII",RomanNumberConverter.toRoman(8));
    }
    @Test
    public void itShouldReturnX_Given10()
    {
        Assert.assertEquals("X",RomanNumberConverter.toRoman(10));
    }
    @Test
    public void itShouldReturnXX_Given20()
    {
        Assert.assertEquals("XX",RomanNumberConverter.toRoman(20));
    }
    @Test
    public void itShouldReturnIV_Given4()
    {
        Assert.assertEquals("IV",RomanNumberConverter.toRoman(4));
    }
    @Test
    public void itShouldReturnIX_Given4()
    {
        Assert.assertEquals("IX",RomanNumberConverter.toRoman(9));
    }
}
