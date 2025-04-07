# A Sample App Using Yhttp Framework  
**This project implement some common apis using yhttp-framework**

### Install Dependencies:
1. Install and activate [postgresql](https://www.w3schools.com/postgresql/postgresql_install.php) on your system
**Note:** keep in your minde, after installing and activation of postgresql
you must do some additional steps to make this project work:
```
echo "CREATE USER ${USER} WITH CREATEDB;" | sudo -u postgres psql
sudo -u postgres psql -c "GRANT postgres TO ${USER};"
```

2. Then you must install [python-makelib](https://github.com/pylover/python-makelib.git)

### Clone the project:
Use `clone` command to get the project,then navigate to the project directory:
```
git clone https://github.com/amirhossein226/yhttp-app-sample.git
cd yhttp-app-sample
```

### Use `make` to prepare your environment:
Thanks to `python-makelib` you can prepare your invironment using bellow
commands:
```
make venv
make activate.sh
source activate.sh
make env
```

### Insert mockups:
By doing previous steps and making sure about installation of `postgresql`, you
will be able to use some command related to project.
1. First step is preparation of your database, thanks to `yhttp-dbmanager`'s
command line interface, you can do this by using `bee db` command:
```
bee db create
bee db objects create
```
2. Then you can use custom `insert-mockup` command to create some data on
   your database to test the application:
```
bee db insert-mockup
```

### Test Apis:
- First run the server using `bee serve` command. 
- You can use `curl` command to make request to the below endpoints:
  - GET >>> localhost:8080/contacts/
  - GET >>> localhost:8080/contacts/1
  - CREATE >>> localhost:8080/contacts
  - UPDATE >>> localhost:8080/contacts/1
  - DELETE >>> localhost:8080/contacts/1
  
