#Internet forum

## Purpose of the project:
The goal of the project is to design an internet forum. The website is to be created by the community, not just by one author - the forum owner.
The project should include functionalities that allow for integration of the associated community in the form of creating extensive threads, short questions, and comments.

### Specific objectives:
* User profile edition.
* New project adding form.
* Editing and deleting added projects by the author or administrator.
* Like counter of a given thread.
* Comments section.
* Ability to add short questions.

### Functionalities:
* Adding projects
* Editing projects
* Adding comments to projects
* Adding questions
* Editing questions
* Adding answers to questions
* Projects liking system
* Project search
* Presenting 4 latest projects on the homepage
* Presenting 3 latest questions on the homepage
* Pagination of pages

## Service interface:
<details> <summary> Home screen </summary>
  
The top part of the page is occupied by a menu that allows switching between subpages. Within the banner area, there is a button allowing to go to the user login or registration window. The menu is fully responsive.
  
  ![c3](https://user-images.githubusercontent.com/58951668/121755323-2e83ad80-cb17-11eb-9bef-4354767e0ac9.PNG)
  
The main page presents a collage consisting of the 4 latest posts. Their thumbnail, title (if it fits, up to a maximum of 2 lines), and the number of likes from users are displayed.
  ![c1](https://user-images.githubusercontent.com/58951668/121754718-9802bc80-cb15-11eb-8a85-b5e684c152a9.PNG)
  
Below the collage, the 3 latest questions from users are displayed.
  ![c2](https://user-images.githubusercontent.com/58951668/121754764-b799e500-cb15-11eb-8d2a-1e1045883653.PNG)

On all pages of the application, there is a button to add a new project or question. When hovering over the button, which is familiar to many applications associated with creating a new message, two more buttons are displayed, whose icons are associated with their functionalities.
  ![c4](https://user-images.githubusercontent.com/58951668/121755204-e1074080-cb16-11eb-8fe6-746c31a846ad.png)
  
The page is closed by a footer in an uncommon style. The diagonal lines used in it give the whole thing dynamism and attract the user's attention. The footer contains the most important information, such as the website address, contact details, and links to individual social media.
  ![c5](https://user-images.githubusercontent.com/58951668/121755470-8c17fa00-cb17-11eb-99a6-108bdb690c26.PNG)


</details>
<details> <summary>Login/Registration</summary>
  
The login form is simple and user-friendly.
  ![c6](https://user-images.githubusercontent.com/58951668/121755633-f6309f00-cb17-11eb-943f-75cda62e6680.PNG)

Registration is equally simple. It requires filling in all fields and meeting the appropriate standards.
  ![c7](https://user-images.githubusercontent.com/58951668/121755711-2ed07880-cb18-11eb-838f-8733cb068b9b.PNG)

</details>
<details> <summary>Creating a project</summary>
  
When creating a project, we have two fields that are mandatory to fill in: the title and thumbnail. We have access to ckeditor, which offers features available in traditional text editors, such as formatting (bold, italic, underline, numbered and bulleted lists), tables, block quoting, linking to web resources, inserting graphics, pasting content from Microsoft Word, undoing and redoing operations, and other HTML formatting tools. It also has a built-in spell checking tool.
  ![c8](https://user-images.githubusercontent.com/58951668/121755955-d483e780-cb18-11eb-9b31-ab0944dd4d3b.PNG)

</details>
<details> <summary>Create a question</summary>
Users can also add short questions in addition to projects. They have the same functionalities as projects, with the difference that they can only contain text questions.
  ![c9](https://user-images.githubusercontent.com/58951668/121756210-a18e2380-cb19-11eb-8d56-40e77473c301.PNG)

</details>
<details> <summary>Pagination</summary>
Pagination has been applied for the view of all projects and questions. Its task is to increase the speed of page loading. As a result, the user spends less time loading content that is not needed at the moment. For questions, pagination occurs when their number exceeds 10, while in the case of projects, the limit per page is 6.
  ![c10](https://user-images.githubusercontent.com/58951668/121756396-38f37680-cb1a-11eb-9533-2293e1404f5d.PNG)

</details>
<details> <summary>Project view</summary>
After selecting a project from the homepage or the project view, the user will be taken to the project details page. The view displays the entire content of the posted project. At the top is the project title, followed by the author's information. Additionally, the number of likes and the user's profile picture are displayed. Next, the thumbnail image of the project is shown, followed by the actual project content. The project allows for editing and deletion by the author, as well as deletion by the administrator.
  ![c11](https://user-images.githubusercontent.com/58951668/121756521-aef7dd80-cb1a-11eb-921b-614016122751.PNG)
</details>

<details> <summary>Comments</summary>
The project view also has a comments section. It is equipped with the ability to delete comments by the commenter or the administrator. The comment shows the user's pseudonym, their profile picture, and the content of the comment.
  ![c12](https://user-images.githubusercontent.com/58951668/121756641-1f9efa00-cb1b-11eb-8e29-8d483dae40a7.PNG)

The comment section also exists for questions and is equipped with the same features as the comment section for projects.
  ![c13](https://user-images.githubusercontent.com/58951668/121756785-9936e800-cb1b-11eb-9bb4-8bf99568f896.PNG)

</details>
<details> <summary>Project search</summary>
On all pages of the application, there is a project search field. After entering the full or partial title and pressing the enter key, the project we are looking for will be displayed.
  ![c15](https://user-images.githubusercontent.com/58951668/121769741-9f51b680-cb65-11eb-8d39-7d897c8f54f7.PNG)

</details>

## Database
Database configuration is done through the normal Python module with module-level variables representing Django settings. By default, the configuration uses SQLite. SQLite is included in Python, so nothing needs to be installed to have a database.

### ERD diagram
![app](https://user-images.githubusercontent.com/58951668/114049692-f4362f80-988b-11eb-87ea-1e0195b8b860.png)
![image](https://user-images.githubusercontent.com/58951668/114904786-80aa9a00-9e18-11eb-8976-5cfb72d6db07.png)

### A script to create a database structure
CREATE TABLE "app_thread" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NULL, "date_posted" datetime NOT NULL, "miniature" varchar(100) NOT NULL, "content" text NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "app_thread_likes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "thread_id" integer NOT NULL REFERENCES "app_thread" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "app_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "url" varchar(40) NOT NULL UNIQUE, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "app_commentthread" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "ddate_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "project_id" integer NOT NULL REFERENCES "app_thread" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "app_commentpost" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "ddate_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "post_id" integer NOT NULL REFERENCES "app_post" ("id") DEFERRABLE INITIALLY DEFERRED);

## Technologies used.
The "JDIY.com" application was written in Python using the Django framework. The graphical interface was designed using HTML and CSS syntax. The project also uses the Bootstrap library, which handles most of the presentation layer elements. The CrispyForm library was used to connect Bootstrap with Django forms, so default forms generated by Django have a consistent look with the rest of the application. Additional libraries may be required for the application to function properly if they are not included in the IDE where the project is running. The main libraries that need to be installed are:
- Pillow 8.2.0
pip install Pillow
- django-ckeditor-5 0.0.14
pip install django-ckeditor-5


## Application launch process (step by step)
The project was created using the PyCharm IDE. To run it, simply import the project and set the run configuration to "Django Server" application.

To install all the required libraries, use the requriments.txt file and enter the following fragment into the terminal of our ide.\
```pip install -r requirements.txt```


To run the application, we use the command **python manage.py runserver** in the terminal of our IDE.
![c14](https://user-images.githubusercontent.com/58951668/121757671-97225880-cb1e-11eb-8cf3-69e1b3958ba6.PNG)

## Django administration
One of the most powerful parts of Django is its automatic admin interface. It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site. Its use is recommended for internal management tasks within an organization. It's not intended to be used to build the entire front end of a site. To access the admin interface, you need to add /admin to the URL of your site.
![c18](https://user-images.githubusercontent.com/58951668/121770437-95ca4d80-cb69-11eb-9845-50bd016fcedc.PNG)

We create the administrator using the command in the PyCharm terminal: **python manage.py createsuperuser**

## Final conclusions
Creating a social networking site from scratch requires a good understanding of current trends and functionalities offered by other similar solutions. In addition, it is necessary to show creative ingenuity, apply well-functioning solutions in a new, better version. You can also introduce your own functionalities, but keep in mind that they must be presented in the most user-friendly way possible. The main advantage of the social networking site I created is its ease of use. The user is not overwhelmed by an excess of functions, information, and notifications. Creating this project has definitely expanded my knowledge of designing social networking sites, as well as their implementation.
