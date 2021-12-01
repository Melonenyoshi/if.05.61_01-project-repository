public class Job{
    private String name;
    private Job jobThatDependOnThisJob;

    public Job(String name, Job jobThatDependOnThisJob) {
        this.name = name;
        this.jobThatDependOnThisJob = jobThatDependOnThisJob;
    }

    public Job(String name) {
        this.name = name;
    }

    public Job getDependency() {
        return jobThatDependOnThisJob;
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
