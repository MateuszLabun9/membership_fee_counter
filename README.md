# membership_fee_counter
This project is calculating membership fees based on given informations. 


Aim for this project is to first load organization_structure file and configuration file. In the next step user is asked for a 3 inputs, rent period, rent amount
and name of organization structure. During this step every user input is being validated.
Next step is to calculate membership fee based on given data and show it to user. During user's input stage proper validation is made, in case of not valid input,
proper error message is being displayed, and user is asked to provide value once again.

View of succesful calculation of memberhsip fee:

![image](https://user-images.githubusercontent.com/44081987/183310321-50407be2-76dc-4f5f-9ef3-c26e718d5254.png)

In case of wrong input there is a validation methods which are displaying proper error message to a user and asking to re-enter value as along as it is invalid,
on photo below there is wrong rent period input:

![image](https://user-images.githubusercontent.com/44081987/183310402-9d179e08-4d0d-43a9-a8d7-11e45e4d7849.png)

In case of wrong rent amount input: 

![image](https://user-images.githubusercontent.com/44081987/183310471-69453439-47ff-488e-9bf0-ff7c12ec9996.png)

If given amount does not fit in given range:
  - Minimum rent amount is £25 per week or £110 per month 
  - Maximum rent amount is £2000 per week or £8660 per month 
Then proper error infomration would be displayed to user:

![image](https://user-images.githubusercontent.com/44081987/183311090-c059021e-50e9-4574-8552-780b17d046be.png)

In case of not existing organization name: 

![image](https://user-images.githubusercontent.com/44081987/183310499-fc8f3ff9-e639-46f0-b137-45c23cc9fdcb.png)



This project also includes few test scenarions located in data_model_test.py file as well as 2 configuration files are included. 
Python verion: 3.10
