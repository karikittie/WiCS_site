## The PSU WiCS (Women in Computer Science) Website  

### A Django driven website for organizational information and administration.  

##### Our Mission:  
We encourage and empower women to pursue computer science, and we are dedicated to building an inclusive, supportive community of technical women at Portland State University.  

##### Our Purpose:  
We aim to create opportunities that inspire, educate, and equip women to succeed in their educational and professional development in computer science and technology. We believe in working toward closing the gender gap in technology by creating a supportive network that will encourage women to get involved in events and activities that will connect them to other technical women in the field, and promote their education and success in computer science.  

### Usage Details  
##### Prerequisites:  
- For local building and testing, [Python >= 3.5.2](https://www.python.org/), and [Django >= 1.11](https://www.djangoproject.com/) are required.  
- Python can be installed through your distribution's package manager (reccomended), which should also install pip (python package manager) alongside that. Failing that, installation instructions can be found [on the pip website here](https://pip.pypa.io/en/stable/installing/).  
- Django can be installed through pip with the following command: `pip install Django`.  
  - If this results in errors, superuser privledges (via sudo/su) may be required. Also check that pip is updated to the latest version.  

##### Setup:  
After cloning the repository, run a one-time setup of the required structures in the database with: `python manage.py migrate`.  

##### Running:  
Run `python manage.py runserver 127.0.0.1:8000`, and the site should be visible in your web browser (incognito/privacy mode reccomended for cache issues) at [http://127.0.0.1:8000](http://127.0.0.1:8000)!  

##### Find us on **[Slack](https://wics-psu.slack.com)** (#web-dev) and **[PSU OrgSync](https://orgsync.com/158259/chapter)**!
