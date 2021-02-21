# shop django rest framework
a shop api with django rest framework

## installation
1. install python3 from <a href="https://www.python.org/" target="_blank">here</a> 
1. pip install -r requirements.txt
1. python manage.py migrate
1. python manage.py createsuperuser(insert user name and password)
1. python manage.py runserver
---

# api paths
* [**api/v1/**](#apiv1)
	* [**api/v1/product/**](#apiv1product)
		* [**api/v1/product/?search={query}**](#apiv1productsearchquery)
	* [**api/v1/category/**](#apiv1category)
		* [**api/v1/category/?search={query}**](#apiv1categorysearchquery)
	* [**api/v1/user/**](#apiv1user) 
	* [**api/v1/cart/**](#apiv1cart)
		* [**api/v1/cart/?search={query}**](#apiv1cartsearchquery)
	* [**api/v1/cart/add/**](#apiv1cartadd)
	* [**api/v1/cart/delete/{pk}/**](#apiv1cartdeletepk)
	* [**api/v1/cart/add_one/{pk}/**](#apiv1cartadd_onepk)
	* [**api/v1/cart/reduce_one/{pk}/**](#apiv1cartreduce_onepk)


* [**auth/**](#auth)
	* [**auth/login/**](#authlogin)
		* [**auth/login/refresh/**](#authloginrefresh)
	* [**auth/register/**](#authregister)
	* [**auth/change_password/{pk}/**](#authchange_passwordpk)
	* [**auth/update_profile/{pk}/**](#authupdate_profilepk)
	* [**auth/logout/**](#authlogout)
	* [**auth/change_image/**](#authchange_image)
	* [**auth/delete_profile/{pk}/**](#authdelete_profilepk)

___	
## api/v1/
### api/v1/product/
**Allowed Methods** : GET
<br>**Access Level** : Public
<br>return array of objects of all products in the database that tagged as available. and also have a nested inner object of category that related to it as ForignKey relation.
<br>you can get a specific product object with passing the pk to the end of the path.

#### api/v1/product/?search={query}
**Allowed Methods** : GET
<br>**Access Level** : Public
<br>search in products by given keywords
<br>search by "search" keyword


### api/v1/category/
**allowed methods** : GET
<br>**Access Level** : Public
<br>return objects of categories that admin made.
<br>you can get a specific category object with passing the pk to the end of the path.

#### api/v1/category/?search={query}
**Allowed Methods** : GET
<br>**Access Level** : Public
<br>search in categories by given keywords
<br>search by "search" keyword


### api/v1/user/
**allowed methods** : GET
<br>**Access Level** : Admin
<br>return object of all registered users
<br>you can get specific user object with passing the pk to the end of the path.


### api/v1/cart/
**allowed methods** : GET
<br>**Access Level** : Authorized users
<br>*GET :* return all products in the authenticated user cart

#### api/v1/cart/?search={query}
**Allowed Methods** : GET
<br>**Access Level** : Authorized users
<br>search in user cartitem by given keywords
<br>search by "search" keyword


### api/v1/cart/add/
**allowed methods** : POST
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'quantity', 'product_id'}
<br>*POST :* The data should include fields available if user authorized.

### api/v1/cart/delete/{pk}/
**allowed methods** : DELETE
<br>**Access Level** : Authorized users
<br>*DELETE :* there is no data to send. you should put the pk of products that are in user cart you want to delete in the url instead of *{pk}*

### api/v1/cart/add_one/{pk}/
**allowed methods** : GET
<br>**Access Level** : Authorized users
<br>*GET :* there is no data to send. you should put the pk of products that are in user cart you want to add one to it in the url instead of *{pk}*

### api/v1/cart/reduce_one/{pk}/
**allowed methods** : GET
<br>**Access Level** : Authorized users
<br>*GET :* there is no data to send. you should put the pk of products that are in user cart you want to reduce one from it in the url instead of *{pk}*


## auth/
### auth/login/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'username', 'password'}
<br>*POST :* the data you post should include 'username' and 'password' fields if the user was authorized the access token and the refresh token will return as json.[more information about JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage)

#### auth/login/refresh/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'refresh'}
<br>*POST :* the data you post should include 'refresh' and the value of it should be user refresh token that is sent when user login.

### auth/register/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'username', 'password1', 'password2', 'email', 'first_name', 'last_name'}
<br>*POST :* should include the 'fields' keys and proper value. errors and exceptions handled , should have a proper place to show them in frontend.

### auth/change_password/{pk}/
**allowed methods** : PUT
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'old_password', 'password1', 'password2'}
<br>*PUT :* should include 'fields' keys with proper values. errors and exceptions handled , should have a proper place to show them in frontend.

### auth/update_profile/{pk}/
**allowed methods** : PUT
<br>**Access Level** : Authorized users
<br>**fields :** 'optional': {'username', 'first_name', 'last_name', 'email'}
<br>*PUT :*  should include the authorized user access token. the uniqueness of email and username handled.

### auth/logout/
**allowed methods** : POST
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'refresh_token'}
<br>*POST :* should include the authorized user access token. post user refresh token with 'refresh_token' key to expire the access and refresh token of the given user.

### auth/change_image/{pk}/
**allowed methods** : PUT
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'image'}
<br>*PUT :* should include the authorized user access token

### auth/delete_profile/{pk}/
**allowed methods** : DELETE
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'password'}
<br>*DELETE :* should pass the pk to the end of the url. and also user password to authorize the user .



---
# To-Do:
- [x] add users and configurations
- [x] add CORS and configurations
- [x] Make the cart
- [x] Add JWT authentication system
- [x] add cors and configurations
- [x] check for availability on get method for all products
- [x] Add JWT authentication system
- [x] add product api
- [x] add delete feature for cart
- [x] add documentation
- [x] add CSRF and configurations
- [x] add the math operations for quantity
- [x] Make the cart
- [x] calculate the quantity and valid products to buy
- [x] add search option for product and category 
- [ ] third party register
- [ ] add support 
- [ ] add billing part
- [ ] add educational blog
- [ ] beautify the code
- [ ] add the frontend
