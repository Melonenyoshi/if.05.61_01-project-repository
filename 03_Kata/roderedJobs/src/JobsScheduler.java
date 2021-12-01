import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class JobsScheduler {
    private List<Job> jobs = new LinkedList<>();

    public void registerJob(String jobName) {
        if(!existsInList(jobName)) {
            Job job = new Job(jobName);
            jobs.add(job);
        }
    }
    public void registerJob(String dependentJob,String independentJob) {
        if(!existsInList(independentJob)) {
            Job jobDep = new Job(dependentJob);
            Job jobInd = new Job(independentJob, jobDep);
            jobs.add(jobInd);
        }
    }
    private boolean existsInList(String s)
    {
        for (Job curr: jobs) {
            if(curr.getJobInChain(s) != null)
            {
                return true;
            }
        }
        return false;
    }
    public void sort() {
    }

    public String getList() {
        String result = "";

        for (Job curr: jobs
             ) {
            result += curr.getJobName("");
        }

        return result;
    }
}
