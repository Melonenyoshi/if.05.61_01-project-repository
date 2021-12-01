import org.junit.Assert;
import org.junit.Test;

public class JobsSchedulerTest {
    @Test
    public void itShouldReturnA_GivenA()
    {
        //arrange
        var sut = new JobsScheduler();//systemundertest
        sut.registerJob("A");

        //assert
        Assert.assertEquals("A",sut.getList());
    }

    @Test
    public void itShouldReturnAB_GivenAB()
    {
        //arrange
        var sut = new JobsScheduler();//systemundertest
        sut.registerJob("A");
        sut.registerJob("B");

        //assert
        Assert.assertEquals("AB",sut.getList());
    }

    @Test
    public void itShouldReturnABC_GivenABC()
    {
        //arrange
        var sut = new JobsScheduler();//systemundertest
        sut.registerJob("A");
        sut.registerJob("B");
        sut.registerJob("C");

        //assert
        Assert.assertEquals("ABC",sut.getList());
    }

    @Test
    public void itShouldReturnAB_GivenBDependingOnA()
    {
        //arrange
        var sut = new JobsScheduler();//systemundertest
        sut.registerJob("B","A");

        //assert
        Assert.assertEquals("AB",sut.getList());
    }

    @Test
    public void itShouldReturnABC_GivenCDependingOnB_AndBDependsOnA()
    {
        //arrange
        var sut = new JobsScheduler();//systemundertest
        sut.registerJob("B","A");
        sut.registerJob("C","B");

        //assert
        Assert.assertEquals("ABC",sut.getList());
    }
    @Test
    public void itShouldReturnAB_GivenABB()
    {
        //arrange
        var sut = new JobsScheduler();//systemundertest
        sut.registerJob("A");
        sut.registerJob("B");
        sut.registerJob("B");

        sut.sort();
        //assert
        Assert.assertEquals("AB",sut.getList());
    }

    @Test
    public void itShouldReturnABC_GivenBDependingOnA_AndCDependsOnB()
    {
        //arrange
        var sut = new JobsScheduler();//systemundertest
        sut.registerJob("C","B");
        sut.registerJob("B","A");

        //assert
        Assert.assertEquals("ABC",sut.getList());
    }

    @Test
    public void itShouldReturnBA_GivenBA()
    {
        //arrange
        var sut = new JobsScheduler();//systemundertest
        sut.registerJob("B");
        sut.registerJob("A");

        //assert
        Assert.assertEquals("BA",sut.getList());
    }
    @Test
    public void itShouldReturnNothing_GivenAdependsOnBAndBDependsOnA()
    {
        //arrange
        var sut = new JobsScheduler();//systemundertest
        sut.registerJob("A","B");
        sut.registerJob("B","A");

        //assert
        Assert.assertEquals("",sut.getList());
    }
    @Test
    public void complexTest1()
    {
        //arrange
        var sut = new JobsScheduler();//systemundertest
        sut.registerJob("A");
        sut.registerJob("B","A");
        sut.registerJob("C","A");
        sut.registerJob("D","C");
        sut.registerJob("Y","X");
        sut.registerJob("Z");

        //assert
        Assert.assertEquals("ABCDXYZ",sut.getList());
    }
}