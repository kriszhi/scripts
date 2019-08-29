#import boto3

#define the connection
#ec2 = boto3.resource('ec2')

def lambda_handler():
    # Use the filter() method of the instances collection to retrieve
    # all running EC2 instances.
    filters = [{
            'Name': 'tag:K8s',
            'Values': ['yes']
        }]
    
    #filter the instances
    instances = ec2.instances.filter(Filters=filters)

    #locate all running instances
    RunningInstances = [instance.id for instance in instances]
    
    #print the instances for logging purposes
    #print RunningInstances 
    
    #make sure there are actually instances to shut down. 
    if len(RunningInstances) > 0:
        #perform the shutdown
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).stop()
        print (shuttingDown)
        SMS()
    else:
        print ("Nothing to see here")
		
def SMS():

    from twilio.rest import Client

    # the following line needs your Twilio Account SID and Auth Token
    client = Client("xxxx", "xxxx")
    
    # change the from_ number to your Twilio number and the to number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(to="+919750818186", 
                           from_="+14052954947", 
                           body="Your AWS Instances Shutdown properly and you done a great job" )
                           
                           
SMS()
