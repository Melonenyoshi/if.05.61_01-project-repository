import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class JobsScheduler {
    private List<Job> jobs = new LinkedList<>();

    public void registerJob(String jobName) {
        if(getIfExistsInList(jobName) == null) {
            Job job = new Job(jobName);
            jobs.add(job);
        }
    }
    public void registerJob(String dependentJob,String independentJob) {
        Job jobDep = new Job(dependentJob);
        Job inListItemDep = getIfExistsInList(dependentJob);
        Job inListItemIndep = getIfExistsInList(independentJob);
        if(inListItemIndep != null && inListItemDep != null)
        {
            //loop error
            return;
        }
        if(inListItemIndep != null)
        {
            inListItemIndep.addJobThatDependsOnThisJob(jobDep);
        }
        else {
            Job jobInd = new Job(independentJob);
            if(inListItemDep != null)
            {
                jobs.add(jobInd);
                jobs.remove(inListItemDep);
                jobInd.addJobThatDependsOnThisJob(inListItemDep);
            }
            else{
                jobInd.addJobThatDependsOnThisJob(jobDep);
                jobs.add(jobInd);
            }
        }
    }
    private Job getIfExistsInList(String s)
    {
        for (Job curr: jobs) {
            if(curr.getJobInChain(s) != null)
            {
                return curr;
            }
        }
        return null;
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
