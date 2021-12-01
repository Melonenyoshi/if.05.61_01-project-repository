import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class JobsScheduler {
    private List<Job> jobs = new LinkedList<>();
    public void registerJob(String jobName) {
        Job job = new Job(jobName);
        if(!jobs.contains(job))
        {
            jobs.add(job);
        }
    }
    public void registerJob(String dependentJob,String independentJob) {
        Job jobIndi = new Job(independentJob);
        Job jobdep = new Job(dependentJob,jobIndi);
        if(!jobs.contains(jobdep))
        {
            jobs.add(jobdep);
        }
    }

    public void sort() {
        jobs = jobs.stream().sorted().collect(Collectors.toList());
    }

    public String getList() {
        String result = "";

        for (Job curr: jobs
             ) {
            result += curr.getName();
        }

        return result;
    }
}
