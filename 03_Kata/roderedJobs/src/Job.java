import java.util.LinkedList;
import java.util.List;

public class Job{
    private String name;
    private List<Job> jobsThatDependOnThisJob = new LinkedList<>();

    public Job(String name, Job givenJobDependingOnThisJob) {
        this.name = name;
        if(givenJobDependingOnThisJob != null)
        {
            this.jobsThatDependOnThisJob.add(givenJobDependingOnThisJob);
        }
    }

    public Job(String name) {
        this(name,null);
    }

    public Job getJobInChain(String s)
    {
        if(s == name)
        {
            return this;
        }
        else{
            if(!jobsThatDependOnThisJob.isEmpty())
            {
                for (Job curr: jobsThatDependOnThisJob
                     ) {
                    Job gottenJob = curr.getJobInChain(s);
                    if(gottenJob != null)
                    {
                        return gottenJob;
                    }
                }
                return null;
            }
            else{
                return  null;
            }
        }
    }
    public void addJobThatDependsOnThisJob(Job job)
    {
        if(job != null)
        {
            this.jobsThatDependOnThisJob.add(job);
        }
    }

    public String getJobName(String s) {
        s = name;

        if(!jobsThatDependOnThisJob.isEmpty())
        {
            for (Job curr: jobsThatDependOnThisJob
                 ) {
                s+= curr.getJobName(s);
            }
        }
        return s;
    }
}
