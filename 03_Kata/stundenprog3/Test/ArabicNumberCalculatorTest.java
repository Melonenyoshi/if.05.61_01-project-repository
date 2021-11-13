import org.junit.Assert;
import org.junit.Test;

public class ArabicNumberCalculatorTest {
    @Test
    public void itShouldReturn1GivenI()
    {
        Assert.assertEquals(1,RomanNumberConverter.toArabic("I"));
    }
    @Test
    public void itShouldReturn2GivenII()
    {
        Assert.assertEquals(2,RomanNumberConverter.toArabic("II"));
    }
    @Test
    public void itShouldReturn3GivenIII()
    {
        Assert.assertEquals(3,RomanNumberConverter.toArabic("III"));
    }
    @Test
    public void itShouldReturn4GivenIV()
    {
        Assert.assertEquals(4,RomanNumberConverter.toArabic("IV"));
    }
    @Test
    public void itShouldReturn5GivenV()
    {
        Assert.assertEquals(5,RomanNumberConverter.toArabic("V"));
    }
    @Test
    public void itShouldReturn100GivenC()
    {
        Assert.assertEquals(100,RomanNumberConverter.toArabic("C"));
    }
    @Test
    public void itShouldReturn183GivenCLXXXIII()
    {
        Assert.assertEquals(183,RomanNumberConverter.toArabic("CLXXXIII"));
    }
    @Test
    public void itShouldReturn99GivenXCIX()
    {
        Assert.assertEquals(99,RomanNumberConverter.toArabic("XCIX"));
    }
    @Test
    public void itShouldReturn536GivenDXXXVI()
    {
        Assert.assertEquals(536,RomanNumberConverter.toArabic("DXXXVI"));
    }
    @Test
    public void itShouldReturn387GivenCCCLXXXVII()
    {
        Assert.assertEquals(387,RomanNumberConverter.toArabic("CCCLXXXVII"));
    }
}
