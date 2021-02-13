# shop django rest framework
a shop api with django rest framework

## Instalation
1. install python3 from <a href="https://www.python.org/" target="_blank">here</a> 
1. pip install -r requirements.txt
1. python manage.py migrate
1. python manage.py createsuperuser(insert user name and password)
1. python manage.py runserver
---

# api paths
* [**api/v1/**](#apiv1)
	* [**api/v1/product/**](#apiv1product)
	* [**api/v1/category/**](#apiv1category) 
	* [**api/v1/user/**](#apiv1user) 
	* [**api/v1/cart/**](#apiv1cart) 
	* [**api/v1/cart/add/**](#apiv1cartadd) 


* [**auth/**](#auth)
	* [**auth/login/**](#authlogin)
		* [**auth/login/refresh/**](#authloginrefresh)
	* [**auth/register/**](#authregister)
	* [**auth/change_password/{pk}/**](#authchange_passwordpk)
	* [**auth/update_profile/{pk}/**](#authupdate_profilepk)
	* [**auth/logout/**](#authlogout)
	* [**auth/change_image/**](#authchange_image)

___	
## api/v1/
### api/v1/product/
**Allowed Methods** : GET
<br>**Access Level** : Public
<br>return array of objects of all products in database that tagged as available. and also have a nested inner object of category that related to it as ForignKey relation.
<br>you can get specific product object with passing the pk to the end of the path.

### api/v1/category/
**allowed methods** : GET
<br>**Access Level** : Public
<br>return objects of categories that admin made.
<br>you can get specific category object with passing the pk to the end of the path.

### api/v1/user/
**allowed methods** : GET
<br>**Access Level** : Admin
<br>return object of all registered users
<br>you can get specific user object with passing the pk to the end of the path.

### api/v1/cart/
**allowed methods** : GET, POST
<br>**Access Level** : Authorized users
<br>*GET :* return all products in the authenticated user cart

### api/v1/cart/add/
**allowed methods** : POST
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'quantity', 'product_id'}
<br>*POST :* the data should include fields available if user authorized.

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
<br>*POST :* the data you post should include 'refresh' and the value of it should be refresh token that send when user login.

### auth/register/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'username', 'password1', 'password2', 'email', 'first_name', 'last_name'}
<br>*POST :* should include the 'fields' keys and proper value. errors and exeptions handled , should have a proper place to show them in frontend.

### auth/change_password/{pk}/
**allowed methods** : PUT
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'old_password', 'password1', 'password2'}
<br>*PUT :* sould include 'fields' keys with proper values. errors and exeptions handled , should have a proper place to show them in frontend.

### auth/update_profile/{pk}/
**allowed methods** : PUT
<br>**Access Level** : Authorized users
<br>**fields :** 'optional': {'username', 'first_name', 'last_name', 'email'}
<br>*PUT :*  should include the authorized user access token. the uniqueness of email and username handeled.

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

---
# To-Do:
- [x] add users and configurations
<<<<<<< HEAD
- [x] add CORS and configurations
- [ ] add CSRF and configurations
- [x] Make the cart
- [ ] add the math operations for quantity
- [ ] narrow the products to 'Available'
- [ ] add educational blog
- [ ] add support 
- [x] Add JWT authentication ystem
=======
- [x] add cors and configurations
- [ ] Make the cart
- [ ] calculate the quantity and valid products to buy
- [ ] check for availability on get method for all products
- [ ] add search option for product and category 
- [x] Add JWT authentication system
>>>>>>> bf485d37f14b78044e4cc9be951dae375a93075d
- [x] add product api
- [x] add delete feature for cart
- [ ] add billing part
- [ ] third party register
- [ ] beautify the code
- [x] add documentation
- [ ] add the frontend
