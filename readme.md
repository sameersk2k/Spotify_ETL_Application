# Spotify ETL Project - Playlist Recommendation - AWS, Spotify API, Terraform and Python

<img width="766" alt="Screenshot 2023-07-30 at 7 19 31 PM" src="https://github.com/sameersk2k/Spotify_ETL_Application/assets/115322069/15a490a5-af13-4b12-9d68-eb91db9b6cc5">

- This is a project focused on learning how to built ETL Pipeline in AWS and deploy using Terraform.
- We have taken Spotify API and extracted data to provide new playlists suggestions based on a provided old playlist of an individual
- One should have an IAM user initialized before starting the project.

## Contents
0. [Introduction](#introduction)
1. [Installation](#installation) 
2. [Usage](#usage)
3. [Project Architecture](#projectarchitecture)
4. [Important Commands/steps](#important)

<a name="introduction"></a>
## Introduction 

Welcome to Spotify Analysis. 
Enjoy learning more about the music you listen to and your personal listening habits.


<a name="installation"></a>
## Installation 

#### Pre-Requisites
[Python](https://www.python.org/downloads/), [Terraform](https://www.terraform.io/downloads.html) and [Spotipy](https://spotipy.readthedocs.io/en/2.13.0/).


<a name="usage"></a>
## Usage 
Run the scripts with a dictionary of your faovurite artists or playlists to gather data about them and save it locally or in S3.

<a name="projectarchitecture"></a>
## Project Architecture 

The Terraform scripts build:
- A lambda function with the analysis code
- A cloudwatch alarm to run that function weekly
- All relevant IAM policies / roles

This will generate a datalake of Spotify data locally or in S3.

<a name="important"></a>
### Important points

- create s3 bucket before deploying lambda function
- use these commands to set environment variables
  ```
  export SPOTIPY_CLIENT_ID=""
  export SPOTIPY_CLIENT_SECRET=""
  ```
- After you create your .tf folder and write providers.tf you have to execute the below command while inside .tf
  ```
  terraform init
  ```
- After all other files are written execute this command to format any syntax errors.
  ```
  terraform fmt
  ```
- I have given a file in .tf with .sh extension execute it to create zip folder payload.zip which will be required to implement lambda in AWS portal.
- After that finally execute this command.
  ```
  terraform apply
  ```
