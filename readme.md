### What is this?
If you type something in any language supported by Google Translate, this program will display a translation into a randomly chosen language and give you 5 options as to what the new language is, while keeping a tally of your correct and incorrect answers.

### Instructions for running this program:
(updated March 2020 on Ubuntu Linux; terminal commands may differ in your OS)

* Download and save the repository folder on your computer

* If needed, install Python 3, Pip3 (for Python modules), and the Google Translate module

  `sudo apt-get install python3`

  `sudo apt-get install pip3`

  `sudo pip3 install google-cloud-translate`
  
* Download a JSON file with a valid API key for Google Translate [here](https://cloud.google.com/translate/docs/quickstart?csw=1). Click the button to set up a project, and follow the bulleted steps listed under the button. You will need a paying Google account, but new users get more than enough credit to cover this.

* Save the JSON file in the program folder or elsewhere (make sure it doesn't become publicly available)

* For each new terminal session, enter the following, depending on where you've saved the JSON file:

  `export GOOGLE_APPLICATION_CREDENTIALS="[your_filename].json"`

* Run the program

  `python3 program.py`
