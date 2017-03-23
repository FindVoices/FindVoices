# FindVoices
Tools for finding what people are saying in a particular location.

Currently hard-coded to search for Twitter commentary on ACA and Health Insurance in the Columbus and Cleveland area.

The big idea:
1. Pick a target location - say "waffling Senator's home state"
1. Create a wide search of tweets about a topic like the ACA repeal within that location.
1. Manually select tweets from people who are personally affected / have a story to share.
1. Pass the list to local organisers who can
   - Vet their story, and see if they want help sharing it
   - Amplify it - if they are interested, set up meetings, press conferences, tell about town halls, help write letter to the editor, etc.

This tool is to do the first three steps.  We assume a spreadsheet will work OK for followup by organizers.


Usage:
- python findvoices/searches.py

You will need to provide your Twitter authorization, which can be done by running the command:
- python findvoices/oauth.py
