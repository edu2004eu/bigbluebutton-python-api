BigBlueButton Python API
------------------------

The work of this project is derivated from https://github.com/schallis/django-bigbluebutton 98f2259fa3 by Steve Challis.

It is a wrapper for accessing the API of bigbluebutton http://code.google.com/p/bigbluebutton/wiki/API


A simple example:

.. code-block:: python

   import argparse
   from bigbluebutton import MeetingSetup, Meeting
   import bbb_settings



   if __name__ == '__main__':
       PARSER = argparse.ArgumentParser(description='creates and join a session')
       PARSER.add_argument('--meeting_name', dest="meeting_name", type=str, required=True,
                            help='name of the meeting')
       PARSER.add_argument('--meeting_id', dest='meeting_id', required=True,
                           help='id for the meeting')
       PARSER.add_argument('--moderator', dest='moderator', required=True,
                           help='name of the meeting moderator')
       PARSER.add_argument( '--moderator_password', dest='moderator_password', required=True,
                           help='password for moderator')
       PARSER.add_argument( '--attendee_password', dest='attendee_password', required=True,
                           help='password for attendee')
       PARSER.add_argument( '--url', dest='url', required=True,
                           help='pre upload url')

       ARGS = PARSER.parse_args()

       session = MeetingSetup(bbb_settings.BBB_API_URL, bbb_settings.SALT,
                              ARGS.meeting_name, ARGS.meeting_id,
                              ARGS.attendee_password, ARGS.moderator_password,
                              pre_upload_slide=ARGS.url)
       session.create_meeting()
       print("meeting expires if noone joins in")

       meeting = Meeting(bbb_settings.BBB_API_URL, bbb_settings.SALT)
       print("MODERATOR:")
       print(meeting.join_url(ARGS.meeting_id, ARGS.moderator, ARGS.moderator_password))
       print('-------------------------------------------')

       print("RANDOM USER:")
       print(meeting.join_url(ARGS.meeting_id, 'RANDOM', ARGS.attendee_password))
       print('-------------------------------------------')

       print("ALL MEETINGS")
       print(meeting.get_meetings())
       print('-------------------------------------------')

       print("IS RUNNING (meeting is only running after someone has joined in)")
       print(meeting.is_running(ARGS.meeting_id))
       print('-------------------------------------------')

       print("END MEETING URL")
       print(meeting.end_meeting_url(ARGS.meeting_id, ARGS.moderator_password))
       print('-------------------------------------------')


       if meeting.is_running(ARGS.meeting_id):
           print("END MEETING")
           meeting.end_meeting(ARGS.meeting_id, ARGS.moderator_password)
           print('-------------------------------------------')
