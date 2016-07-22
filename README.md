# School System

## How to use the program

You have to run  ```main.py```

## User stories implemented:

1) System / Handle new application

2) System / Find possible interview date

3) Applicant view / Application

4) Applicant view / Interview

6) Administrator view / Applicants


## The Story

We're the developers of a new programming school which has an amazing number of new applicants every day :-) Let's call it Codecool!

Our primary goal is to handle incoming applications and write a software, a console application which helps the following workflow:

1.) A new applicant arrives

2.) We generate a unique application code for her (it helps to track the applicant)

3.) Based on the location information we find the closest Codecool School which will evaluate her application

4.) Based on the mentors' availability in that School, we find a possible interview date where she can convince us about her motivation

5.) Based on the interview result, the interviewer (mentor) accepts or rejects the application

6.) The applicant checks her final status/result


Applicants have a lot of questions during this application process.

Our additional goal is to extend the software and to provide a workflow for incoming questions also:

1.)A new question arrives (from any applicant)

2.)Administrators check the incoming questions and assign them to mentors

3.)Mentors get the questions and answer them

4.)Applicants get the answers



## Technical details

In this project we will use the following technologies:

1.) Python (for writing the software)

2.) PostgreSQL (for storing all the data)

3.) Peewee ORM (to map the data and use objects)




##### It's required to work with at least the following Models:

-Applicant

-School

-City

-Mentor

-InterviewSlot

-Interview

-Question

-Answer
