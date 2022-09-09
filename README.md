# Roomate-Matcher

1. Clone this GitHub repository or [download the zip file](https://github.com/akhil-datla/Roommate-Matcher/archive/refs/heads/main.zip).

2. [Edit the group size](https://github.com/akhil-datla/Roommate-Matcher/blob/main/main.py#L7) (default: 4).

3. Download [pip](https://pip.pypa.io/en/stable/installation/) if you need to.

4. Open Terminal or Command Prompt and navigate to the directory with the program files. 

5. Run `pip install -r requirements.txt`.

6. Create a Google Form with the following questions. **NOTE: ENABLE THE `Collect email addresses` OPTION. QUESTIONS MARKED REQUIRED(*) ARE REQUIRED FOR THE PYTHON PROGRAM. QUESTIONS MUST MATCH THE CASE AND THE WORDING AS SHOWN IN THE IMAGE.**

<img width="430" alt="Google Form Questionnaire" src="https://user-images.githubusercontent.com/66145155/171505113-8369ce68-fcdd-4066-92b7-139e056b36aa.png">

7. Check the corresponding Google Sheet and ensure all the fields present in the following image are the the same as yours.

<img width="1126" alt="Screen Shot 2022-06-01 at 2 31 47 PM" src="https://user-images.githubusercontent.com/66145155/171505374-3c4b0403-4e09-43de-8d95-c46dcfc78acf.png">

8. Download the CSV file of the spreadsheet.

9. Run `python main.py <CSV file path>`. **NOTE: Replace `<CSV file path>` with the path to the CSV file of the spreadsheet.**

After the program runs successfully, a new file called `rooms.csv` will be generated with the room assignments.

