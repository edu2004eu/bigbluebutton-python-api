# BigBlueButton Python API

The work of this project is forked from https://hg.sr.ht/~dreimark/bigbluebutton-python-api
which in turn is derived from https://github.com/schallis/django-bigbluebutton 98f2259fa3 by Steve Challis.

It is a wrapper for accessing the API of BigBlueButton https://docs.bigbluebutton.org/dev/api.html

## Installation

    pip install bigbluebutton-api


## Usage

Here are a few things you can do with this library.

    from bigbluebutton import BigBlueButton
    bbb = BigBlueButton('<YOUR_BBB_URL>', '<YOUR_BBB_SALT>')
    meeting_id = 'some-meeting-id'
    bbb.create_meeting(meeting_id, 'Some meeting name', 'attendee password', 'moderator password')

    moderator_link = meeting.join_meeting_url(meeting_id, 'Example Moderator', 'moderator password'))
    attendee_link = meeting.join_meeting_url(meeting_id, 'Example Attendee', 'attendee password'))

    all_meetings = meeting.get_meetings()
    is_running = meeting.is_running(meeting_id)
    end_link = meeting.end_meeting_url(meeting_id, 'moderator password')

    if meeting.is_running(meeting_id):
        meeting.end_meeting(meeting_id, 'moderator password')

#### Disclaimer

I have absolutely no experience with publishing packages to PyPI and with copyright / attributions. I don't intend
to step on anyone's toes, I just felt like the original library needed a few bugfixes and improvements.

If you feel I haven't recognized your work on this project, please [let me know](mailto:edu2004eu@gmail.com).

I don't plan on further maintaining this package, unless the BBB API changes enough to break it. We do use this
in production, however I can't guarantee everything works (we mainly use the `create` and `join` calls). I can, however,
review any PRs and accept new contributors (after a few approved PRs).