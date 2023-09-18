from collections import defaultdict

def read_file(filepath: str):
    file = open(filepath, 'r')
    num_jobs = int(file.readline())
    
    Lines = file.readlines()
    job_list = []
    for Line in Lines:
        a = Line.split(' ')
        job = []
        for i in a:
            job.append(int(i))
        job_list.append(job)
                 
    return num_jobs, job_list


# decreasing order of (weight - len)
def job_schedule1(job_list):
    # Generate key(weight - len) list, dict
    k1 = []
    k1_dict = dict()
    
    sorted_job_list = sorted(job_list, key=lambda x: x[0], reverse=True)
    
    for i in sorted_job_list:
        key = i[0] - i[1]
        if key not in k1:
            k1.append(key)
            k1_dict[key] = [i]
        else:
            k1_dict[key].append(i)
    
    # sort by (weight - len)
    k1_sorted = sorted(k1, reverse = True)
    
    # calculate weighted sum
    accumulated_time = 0
    weighted_sum = 0
    
    for i in k1_sorted:
        if len(k1_dict[i]) > 1:
            for job in k1_dict[i]:
                accumulated_time += job[1]
                weighted_sum += job[0] * accumulated_time
        else:
            accumulated_time += k1_dict[i][0][1]
            weighted_sum += k1_dict[i][0][0]
    
    return weighted_sum


# decreasing order of (weight / len)
def job_schedule2(job_list):
    # Generate key(weight / len) list, dict
    k1 = []
    k1_dict = dict()
    
    sorted_job_list = sorted(job_list, key=lambda x: x[0], reverse=True)
    
    for i in sorted_job_list:
        key = i[0]/i[1]
        if key not in k1:
            k1.append(key)
            k1_dict[key] = [i]
        else:
            k1_dict[key].append(i)
    
    # sort by (weight / len)
    k1_sorted = sorted(k1, reverse = True)
    
    # calculate weighted sum
    accumulated_time = 0
    weighted_sum = 0

    for i in k1_sorted:
        if len(k1_dict[i]) > 1:
            for job in k1_dict[i]:
                accumulated_time += job[1]
                weighted_sum += job[0] * accumulated_time
        else:
            accumulated_time += k1_dict[i][0][1]
            weighted_sum += k1_dict[i][0][0]
    
    return weighted_sum


def main():
    job_list = read_file('Chapter3\\3-1 Job Scheduling.txt')[1]
    weighted_sum1 = job_schedule1(job_list)
    weighted_sum2 = job_schedule1(job_list)
    return print(weighted_sum1, weighted_sum2)

if __name__ == '__main__':
    main()