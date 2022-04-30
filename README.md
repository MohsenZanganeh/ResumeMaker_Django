# ResumeMaker with Django
## it's just a training project

## we have three kind of users:
### - Admin
### - Employee
### - Candidate

when you register with one of Employee and Candidate types
you must first complete your registration.

### if you're a Candidate
- you can create Work Experience `127.0.0.1:8000/candidates/work_experience/`
- you can create skill `127.0.0.1:8000/candidates/skill/`
- you can create Language `127.0.0.1:8000/candidates/language/`
- you can apply for a job `127.0.0.1:8000/applying/applied_job/`


### if you're a Employee
- you can create job `127.0.0.1:8000/employees/job`
- you can accept the applied jobs `127.0.0.1:8000/applying/applied_job/`