public class Job{
    private String name;
    private Job jobThatDependOnThisJob;

    public Job(String name, Job jobThatDependOnThisJob) {
        this.name = name;
        this.jobThatDependOnThisJob = jobThatDependOnThisJob;
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
            if(jobThatDependOnThisJob != null)
            {
                return this.jobThatDependOnThisJob.getJobInChain(s);
            }
            else{
                return  null;
            }
        }
    }

    public String getJobName(String s) {
        s += name;
        if(jobThatDependOnThisJob != null)
        {
            return jobThatDependOnThisJob.getJobName(s);
        }
        return s;
    }

}
