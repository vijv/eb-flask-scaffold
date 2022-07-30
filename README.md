# eb-flask-scaffold
Elastic Beanstalk Flask application with CD

### eb init
- It added entries into `.gitignore`
- Created `.elasticbeanstak` folder
- `config.yml` inside `.elasticbeanstalk` folder created with initial config with `eb-flask-scaffold` application name


### eb create

*This didn't work with app.py, had to name it application.py*

```
(.eb-flask-scaffold) Vaibhavs-MBP:eb-flask-scaffold vaibhavvij$ eb create
Enter Environment Name
(default is eb-flask-scaffold-dev):
Enter DNS CNAME prefix
(default is eb-flask-scaffold-dev):

Select a load balancer type
1) classic
2) application
3) network
(default is 2):


Would you like to enable Spot Fleet requests for this environment? (y/N): y
Enter a list of one or more valid EC2 instance types separated by commas (at least two instance types are recommended).
(Defaults provided on Enter):


2.0+ Platforms require a service role. We will attempt to create one for you. You can specify your own role using the --service-role option.
Type "view" to see the policy, or just press ENTER to continue:
Creating application version archive "app-0cbd-220730_160858505669".
Uploading eb-flask-scaffold/app-0cbd-220730_160858505669.zip to S3. This may take a while.
Upload Complete.
Environment details for: eb-flask-scaffold-dev
  Application name: eb-flask-scaffold
  Region: us-east-1
  Deployed Version: app-0cbd-220730_160858505669
  Environment ID: e-npc6hx2ksi
  Platform: arn:aws:elasticbeanstalk:us-east-1::platform/Python 3.7 running on 64bit Amazon Linux 2/3.3.15
  Tier: WebServer-Standard-1.0
  CNAME: eb-flask-scaffold-dev.us-east-1.elasticbeanstalk.com
  Updated: 2022-07-30 08:09:07.061000+00:00
Printing Status:
2022-07-30 08:09:05    INFO    createEnvironment is starting.
2022-07-30 08:09:07    INFO    Using elasticbeanstalk-us-east-1-160443734003 as Amazon S3 storage bucket for environment data.
2022-07-30 08:09:33    INFO    Created target group named: arn:aws:elasticloadbalancing:us-east-1:160443734003:targetgroup/awseb-AWSEB-SUXP7X2HDSB8/c099e38c7962a1d0
2022-07-30 08:09:33    INFO    Created security group named: sg-09c97506eeee81247
2022-07-30 08:09:49    INFO    Created security group named: awseb-e-npc6hx2ksi-stack-AWSEBSecurityGroup-105DUJHKIP99V
2022-07-30 08:11:06    INFO    Created Auto Scaling group named: awseb-e-npc6hx2ksi-stack-AWSEBAutoScalingGroup-96BZZLGNOQIR
2022-07-30 08:11:06    INFO    Waiting for EC2 instances to launch. This may take a few minutes.
2022-07-30 08:11:21    INFO    Created Auto Scaling group policy named: arn:aws:autoscaling:us-east-1:160443734003:scalingPolicy:008cb632-2ae0-4cc4-b224-77ead6ec8cc2:autoScalingGroupName/awseb-e-npc6hx2ksi-stack-AWSEBAutoScalingGroup-96BZZLGNOQIR:policyName/awseb-e-npc6hx2ksi-stack-AWSEBAutoScalingScaleUpPolicy-0Z3wkKSHM3HG
2022-07-30 08:11:21    INFO    Created Auto Scaling group policy named: arn:aws:autoscaling:us-east-1:160443734003:scalingPolicy:c6d9e140-d81e-484c-9806-8c9ae99f7a26:autoScalingGroupName/awseb-e-npc6hx2ksi-stack-AWSEBAutoScalingGroup-96BZZLGNOQIR:policyName/awseb-e-npc6hx2ksi-stack-AWSEBAutoScalingScaleDownPolicy-u4woc0Yu4S9B
2022-07-30 08:11:37    INFO    Created CloudWatch alarm named: awseb-e-npc6hx2ksi-stack-AWSEBCloudwatchAlarmHigh-1SCLJK6KKU4WI
2022-07-30 08:11:37    INFO    Created CloudWatch alarm named: awseb-e-npc6hx2ksi-stack-AWSEBCloudwatchAlarmLow-1TRC2SCDGLB32
2022-07-30 08:12:10    INFO    Created load balancer named: arn:aws:elasticloadbalancing:us-east-1:160443734003:loadbalancer/app/awseb-AWSEB-3QXQ8VAD3Q90/1d13ee8ef4660228
2022-07-30 08:12:25    INFO    Created Load Balancer listener named: arn:aws:elasticloadbalancing:us-east-1:160443734003:listener/app/awseb-AWSEB-3QXQ8VAD3Q90/1d13ee8ef4660228/5e13f24b53feaf43
2022-07-30 08:13:55    INFO    Instance deployment successfully generated a 'Procfile'.
2022-07-30 08:13:58    INFO    Instance deployment completed successfully.
 -- Events -- (safe to Ctrl+C)
```
