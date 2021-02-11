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
**Access Level** : Public
return array of objects of all products in database that tagged as available. and also have a nested inner object of category that related to it as ForignKey relation.
you can get specific product object with passing the pk to the end of the path.

### api/v1/category/
**allowed methods** : GET
**Access Level** : Public
return objects of categories that admin made.
you can get specific category object with passing the pk to the end of the path.

### api/v1/user/
**allowed methods** : GET
**Access Level** : Admin
return object of all registered users
you can get specific user object with passing the pk to the end of the path.

### api/v1/cart/
**allowed methods** : GET, POST
**Access Level** : Authorized users
*GET :* return all products in the authenticated user cart
*POST :*

## auth/
### auth/login/
**allowed methods** : POST
**Access Level** : Public
**fields :** 'required': {'username', 'password'}
*POST :* the data you post should include 'username' and 'password' fields if the user was authorized the access token and the refresh token will return as json.[more information about JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage)

#### auth/login/refresh/
**allowed methods** : POST
**Access Level** : Public
**fields :** 'required': {'refresh'}
*POST :* the data you post should include 'refresh' and the value of it should be refresh token that send when user login.

### auth/register/
**allowed methods** : POST
**Access Level** : Public
**fields :** 'required': {'username', 'password1', 'password2', 'email', 'first_name', 'last_name'}
*POST :* should include the 'fields' keys and proper value. errors and exeptions handled , should have a proper place to show them in frontend.

### auth/change_password/{pk}/
**allowed methods** : PUT
**Access Level** : Authorized users
**fields :** 'required': {'old_password', 'password1', 'password2'}
*PUT :* sould include 'fields' keys with proper values. errors and exeptions handled , should have a proper place to show them in frontend.

### auth/update_profile/{pk}/
**allowed methods** : PUT
**Access Level** : Authorized users
**fields :** 'optional': {'username', 'first_name', 'last_name', 'email'}
*PUT :* the uniqueness of email and username handeled.

### auth/logout/
**allowed methods** : POST
**Access Level** : Authorized users
**fields :** 'required': {'refresh_token'}
*POST :* post user refresh token to expire the access and refresh token of the given user.

### auth/change_image/
**allowed methods** : POST
**Access Level** : Authorized users
**fields :** 'required': {'refresh_token'}
---
# To-Do:
- [x] add users and configurations
- [x] add cors and configurations
- [ ] Make the cart
- [x] Add JWT authentication ystem
- [x] add product api
- [ ] add billing part
- [ ] beautify the code
- [ ] add documentation
- [ ] add the frontend
