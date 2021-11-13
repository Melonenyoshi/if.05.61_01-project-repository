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
}
