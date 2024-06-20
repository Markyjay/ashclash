# Testing

[Click here to go back to the README.md file](README.md)

## Overview

This document outlines the testing process for the Sleep Healthily website. The testing process includes manual testing, performance testing and code validation. The testing process was carried out on Google Chrome, Mozilla Firefox, and Safari on MacBook.

## Table of Contents

- [Validation](#validation)
  - [HTML](#html)
  - [CSS](#css)
  - [Python and Django (Pep 8)](#python-and-django-pep-8)
- [Performance](#performance)
  - [Mobile Performance](#mobile-performance)
  - [Desktop Performance](#desktop-performance)
- [Manual Testing](#manual-testing)
- [Incomplete known bugs and UX improvements](#incomplete-known-bugs-and-ux-improvements)

## Validation

### HTML

I use the [W3C Markup Validation Service](https://validator.w3.org/) to validate my HTML code.

With Django, there's a lot of syntax that doesn't play well with the HTML Validator, such as `{% url 'homepage' %}` or `{{ variable|filter }}`.

Normally, I validate by using [validate by uri](https://validator.w3.org/#validate_by_uri) by passing in my deployed URL. However, many pages on this site require a user to be logged in and authenticated, and will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have access to login to the pages.

In order to properly validate my HTML pages for authenticated pages, I followed these steps:

- Navigate to the deployed pages that require authentication
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire compiled code.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
- Repeat this process for every page that requires a user to be logged-in/authenticated.

| Page             | W3C URL                                                                                                 | Screenshot                                                                         | Notes                                |
| ---------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------ |
| Homepage         | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fashclash-pp5-8ef04402753f.herokuapp.com%2F)       | ![Homepage Validation](documentation/validation/html/homepagevalidation.jpg)       | Pass                                 |
| Products         | NA                                                                                                      | ![Products Validation](documentation/validation/html/productsvalidation.jpg)       | Pass                                 |
| Products Add     | NA                                                                                                      | ![Products Add Validation](documentation/validation/html/productsaddvalidation.jpg)| Pass                                 |
| Product Detail   | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fashclash-pp5-8ef04402753f.herokuapp.com%2Freview%2Fproducts%2F175%2F) | ![Product Detail Validation](documentation/validation/html/productdetailvalidation.jpg)| Pass         |
| Profile          | NA                                                                                                      | ![Profile Validation](documentation/validation/html/profilevalidation.jpg)         | Pass                                 |
| Promotions       | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fashclash-pp5-8ef04402753f.herokuapp.com%2Fpromotions%2Fpromotions%2F) | ![Promotions Validation](documentation/validation/html/promotionvalidation.jpg) | Pass                |
| Create Promotions| [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fashclash-pp5-8ef04402753f.herokuapp.com%2Fpromotions%2Fpromotions%2Fcreate%2F)                   | ![Promotions Add Validation](documentation/validation/html/createpromotionsvalidation.jpg)| Duplicate error ID when using Custom Clearable input from CI Tutorial  |
| Basket           | NA                                                                                                      | ![Basket Validation](documentation/validation/html/basketvalidation.jpg)           | Pass                                 |
| Checkout         | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fashclash-pp5-8ef04402753f.herokuapp.com%2Fcheckout%2F)                | ![Contact Validation](documentation/validation/html/checkoutvalidation.jpg)| Duplicate error ID when using Custom Clearable input from CI Tutorial  |
| Edit Review      | NA                                                                                                       | ![Edit Product Validation](documentation/validation/html/editreviewvalidation.jpg)| Pass                                 |
| Login            | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fashclash-pp5-8ef04402753f.herokuapp.com%2Faccounts%2Fsignup%2F)       | ![Login Validation](documentation/validation/html/loginvalidation.jpg)| Pass                          |
| Logout           | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fashclash-pp5-8ef04402753f.herokuapp.com%2Faccounts%2Flogout%2F)       | ![Order Summary Validation](documentation/validation/html/logoutvalidation.jpg)| Scope error due to Bootstrap 4 syntax   |
| Signup           | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fashclash-pp5-8ef04402753f.herokuapp.com%2Faccounts%2Flogout%2F)       | ![Signup Validation](documentation/validation/html/signupvalidation.jpg) | Pass                       |

### CSS

I use the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate my CSS code. You can [click here to see the validated CSS code without any errors](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fashclash-pp5-8ef04402753f.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en).

### Python and Django (Pep 8)

I used the [Code Institute PEP8 Validator](https://pep8ci.herokuapp.com/) to check that my Python code is PEP8 compliant. I validated any files that were either modified or created by me. Here is a table of the validated code, which shows the file validated, a screenshot, and a description of any warnings: I was unable to find a safe fix for the two fails

| File                        | Screenshot                                                                       | Description                            |
| --------------------------- | -------------------------------------------------------------------------------- | -------------------------------------- |
| ashclash/settings.py        | ![ashclash-settings](documentation/validation/pep8/pep8ashclashsettings.jpg)     | Pass                                   |
| ashclash/urls.py            | ![ashclash-urls](documentation/validation/pep8/pep8ashclashurls.jpg)             | Pass                                   |
| basket/contexts.py          | ![basket-contexts](documentation/validation/pep8/pep8basketcontexts.jpg)         | Pass                                   |
| basket/views.py             | ![basket-views](documentation/validation/pep8/pep8basketviews.jpg)               | Pass                                   |
| basket/urls.py              | ![basket-urls](documentation/validation/pep8/pep8basketurls.jpg)                 | Pass                                   |
| checkout/admin.py           | ![checkout-admin](documentation/validation/pep8/pep8checkoutadmin.jpg)           | Pass                                   |
| checkout/forms.py           | ![checkout-forms](documentation/validation/pep8/pep8checkoutforms.jpg)           | Pass                                   |
| checkout/models.py          | ![checkout-models](documentation/validation/pep8/pep8checkoutmodels.jpg)         | Pass                                   |
| checkout/signals.py         | ![checkout-signals](documentation/validation/pep8/pep8checkoutsignals.jpg)       | Pass                                   |
| checkout/urls.py            | ![checkout-urls](documentation/validation/pep8/pep8checkouturls.jpg)             | Pass                                   |
| checkout/views.py           | ![checkout-views](documentation/validation/pep8/pep8checkoutviews.jpg)           | E501 line too long (81 > 79 characters)|
| checkout/webhook_handler.py | ![checkout-webhook_handler](documentation/validation/pep8/pep8checkoutWHH.jpg)   | E501 line too long (81 > 79 characters)|
| checkout/webhooks.py        | ![checkout-webhooks](documentation/validation/pep8/pep8checkoutWHS.jpg)          | Pass                                   |
| product/admin.py            | ![product-admin](documentation/validation/pep8/pep8productadmin.jpg)             | Pass                                   |
| product/forms.py            | ![product-forms](documentation/validation/pep8/pep8productforms.jpg)             | Pass                                   |
| product/models.py           | ![product-models](documentation/validation/pep8/pep8productmodels.jpg)           | Pass                                   |
| product/urls.py             | ![product-urls](documentation/validation/pep8/pep8producturls.jpg)               | Pass                                   |
| product/views.py            | ![product-views](documentation/validation/pep8/pep8productviews.jpg)             | Pass                                   |
| product/widgets.py          | ![product-widgets](documentation/validation/pep8/pep8productwidgets.jpg)         | Pass                                   |
| profiles/forms.py           | ![profiles-forms](documentation/validation/pep8/pep8profileforms.jpg)            | Pass                                   |
| profiles/models.py          | ![profiles-models](documentation/validation/pep8/pep8profilemodels.jpg)          | Pass                                   |
| profiles/urls.py            | ![profiles-urls](documentation/validation/pep8/pep8profileurls.jpg)              | Pass                                   |
| profiles/views.py           | ![profiles-views](documentation/validation/pep8/pep8profileviews.jpg)            | Pass                                   |
| promotions/admin.py         | ![profiles-admin](documentation/validation/pep8/pep8promotionsadmin.jpg)         | Pass                                   |
| promotions/forms.py         | ![promotions-forms](documentation/validation/pep8/pep8promotionsforms.jpg)       | Pass                                   |
| promotions/models.py        | ![promotions-models](documentation/validation/pep8/pep8promotionsmodels.jpg)     | Pass                                   |
| promotions/urls.py          | ![promotions-urls](documentation/validation/pep8/pep8promotionsurls.jpg)         | Pass                                   |
| promotions/views.py         | ![promotions-views](documentation/validation/pep8/pep8promotionsviews.jpg)       | Pass                                   |
| home/urls.py                | ![home-urls](documentation/validation/pep8/pep8homeurls.jpg)                     | Pass                                   |
| home/views.py               | ![home-views](documentation/validation/pep8/pep8homeviews.jpg)                   | Pass                                   |
| review/admin.py             | ![review-admin](documentation/validation/pep8/pep8reviewadmin.jpg)               | Pass                                   |
| review/forms.py             | ![review-forms](documentation/validation/pep8/pep8reviewforms.jpg)               | Pass                                   |
| review/models.py            | ![review-models](documentation/validation/pep8/pep8reviewmodels.jpg)             | Pass                                   |
| review/urls.py              | ![review-urls](documentation/validation/pep8/pep8reviewurls.jpg)                 | Pass                                   |
| review/views.py             | ![review-views](documentation/validation/pep8/pep8reviewviews.jpg)               | Pass                                   |


## Performance

Performance metrics were gathered using Google's PageSpeed Insights to ensure the website operates efficiently on both mobile and desktop devices. Below are the performance results with Lighthouse screenshots from the `documentation/performance` directory.

### Mobile Performance

| Page            | Lighthouse Screenshot                                                            | Comments       |
| --------------- | ---------------------------------------------------------------------------------|--------------- |
| Homepage        | ![Homepage Mobile](documentation/performance/lighthouse/mbhomepagelhtest.jpg)    |  84            |
| Login           | ![Login Mobile](documentation/performance/lighthouse/mbloginlhtest.jpg)          |  84            |
| Product Detail  | ![Product Mobile](documentation/performance/lighthouse/mbproductdetaillhtest.jpg)|  82            |
| Products        | ![Products Mobile](documentation/performance/lighthouse/mbproductpagelhtest.jpg) |  73            |
| Search          | ![Search Mobile](documentation/performance/lighthouse/mbsearchlhtest.jpg)        |  70            |
| Promotions      | ![Promotions Mobile](documentation/performance/lighthouse/mbpromotionslhtest.jpg)|  81            |
| Reviews         | ![Reviews Mobile](documentation/performance/lighthouse/mbreviewslhtest.jpg)      |  72            |

### Desktop Performance

| Page            | Lighthouse Screenshot                                                                      | Comments       |
| --------------- | ------------------------------------------------------------------------------------------ | -------------- |
| Homepage        | ![Homepage Desktop](documentation/performance/lighthouse/dthomepagelhtest.jpg)             |  96            |
| Login           | ![Login Desktop](documentation/performance/lighthouse/dtloginlhtest.jpg)                   |  98            |
| Product Detail  | ![Product Detail Desktop](documentation/performance/lighthouse/dtproductdetaillhtest.jpg)  |  98            |
| Products        | ![Products Desktop](documentation/performance/lighthouse/dtproductpagelhtest.jpg)          |  95            |
| Search          | ![Search Desktop](documentation/performance/lighthouse/dtsearchlhtest.jpg)                 |  91            |
| Promotions      | ![Promotions Desktop](documentation/performance/lighthouse/dtpromotionslhtest.jpg)         |  96            |
| Reviews         | ![Reviews Desktop](documentation/performance/lighthouse/dtreviewslhtest.jpg)               |  95            |

## Manual Testing

I carried out manual testing according to my user stories. To be considered a pass, it needs to have met the acceptance criteria. I carried the tests out on Google Chrome, Mozilla Firefox, and Safari on MacBook.

| User story - As an admin, I want to be able to...                                                                            | Notes  | Chrome | Firefox | Safari |
| ---------------------------------------------------------------------------------------------------------------------------- | ------ | :----: | :-----: | :----: |
| **monitor user profiles** to **maintain an accurate user database**.                                                         | Passed |   ✅   |   ✅   |   ✅   |
| **create new products** to **offer more choices to customers**.                                                              | Passed |   ✅   |   ✅   |   ✅   |
| **update product details** to **ensure all information about the products is current and accurate**.                         | Passed |   ✅   |   ✅   |   ✅   |
| **delete products** to **remove items that are no longer available or relevant**.                                            | Passed |   ✅   |   ✅   |   ✅   |
| **to view a list of all promotional player profiles** to **efficiently manage and monitor the product promotions**.          | Passed |   ✅   |   ✅   |   ✅   |
| **to add new player profiles** to **keep the player database current and complete**.                                         | Passed |   ✅   |   ✅   |   ✅   |
| **edit existing player profiles** to **update information as needed**.                                                       | Passed |   ✅   |   ✅   |   ✅   |
| **delete player profiles that are no longer active** to **to maintain a clean and updated player database**.                 | Passed |   ✅   |   ✅   |   ✅   |
| **monitor reviews left by customer** to **keep consider advice given by my consumers**.                                      | Passed |   ✅   |   ✅   |   ✅   |
| **delete reviews** to **keep them relevent and clean**.                                                                      | Passed |   ✅   |   ✅   |   ✅   |


| User story - As a user, I can...                                                                                             | Notes  | Chrome | Firefox | Safari |
| ---------------------------------------------------------------------------------------------------------------------------- | ------ | :----: | :-----: | :----: |
| **create an account** to **access personalised features and save my purchase history**.                                      | Passed |   ✅   |   ✅   |   ✅   |
| **log into my account** to **access my personal settings and order history, or prefill my details at checkout**.             | Passed |   ✅   |   ✅   |   ✅   |
| **log out of my account** to **ensure my account is secure when I'm not using it**.                                          | Passed |   ✅   |   ✅   |   ✅   |
| **access and view my user profile** to **see my personal information, order history, and manage my account settings**.       | Passed |   ✅   |   ✅   |   ✅   |
| **edit and delete my account** to **change or remove my personal data from the platform**.                                   | Passed |   ✅   |   ✅   |   ✅   |
| **search for products** to **find specific items I'm interested in purchasing**.                                             | Passed |   ✅   |   ✅   |   ✅   |
| **sort products by criteria** to **easily find what I'm looking for**.                                                       | Passed |   ✅   |   ✅   |   ✅   |
| **view product details** to **make informed purchase decision**.                                                             | Passed |   ✅   |   ✅   |   ✅   |
| **add products to my basket** to **purchase them**.                                                                          | Passed |   ✅   |   ✅   |   ✅   |
| **update or remove products from my basket** to **manage items before finalizing my purchase**.                              | Passed |   ✅   |   ✅   |   ✅   |
| **view a summary of my orders** to **keep track of my purchases**.                                                           | Passed |   ✅   |   ✅   |   ✅   |
| **complete the checkout process and pay** to **finalise my order**.                                                          | Passed |   ✅   |   ✅   |   ✅   |
| **create reviews for products** to **share my experience with others**.                                                      | Passed |   ✅   |   ✅   |   ✅   |
| **update my reviews** to **modify my feedback if my opinion changes**.                                                       | Passed |   ✅   |   ✅   |   ✅   |
| **delete my reviews** to **remove my feedback if I no longer wish it to be displayed**.                                      | Passed |   ✅   |   ✅   |   ✅   |



## Incomplete known bugs and UX improvements

The below are known bugs and possible areas of UX improvement I came across during testing.

### Known Bugs

Search Functionality Issues:
Issue: Search results do not accurately reflect the user's query, sometimes missing relevant products or including irrelevant ones.
Potential Fix: Refine the search algorithm to better parse and match user queries. Use advanced search techniques like fuzzy search and synonyms matching.

Slow Page Load Times:
Issue: Some pages, especially the product listing pages, load slowly.
Potential Fix: Optimize image sizes, leverage browser caching, and minify CSS/JS files. Consider implementing lazy loading for images and infinite scroll for product listings.

Checkout Process Bugs:
Issue: Some users experience errors during the checkout process, such as payment failures or incorrect order totals.
Potential Fix: Thoroughly test the payment gateway integration and order processing logic. Ensure robust error handling and provide clear feedback to users if an issue occurs.

### UX Improvements
Improved Navigation:
Current Issue: Users find it difficult to navigate between product categories and other sections of the site.
Improvement: Implement a more intuitive and organized navigation menu. Consider adding breadcrumbs and a sticky navigation bar for better user orientation.

Better Mobile Experience:
Current Issue: The mobile version of the site is not fully optimized, with some elements not displaying correctly.
Improvement: Ensure responsive design principles are applied throughout the site. Optimize the layout and interactions for mobile users, including touch-friendly elements and simplified navigation.

Clearer Product Information:
Current Issue: Product descriptions are often lacking detailed information, leading to user confusion.
Improvement: Enhance product descriptions with comprehensive details, including specifications, materials, and usage instructions. Use bullet points for better readability.

Enhanced Review System:
Current Issue: The review system is not prominently featured, number of reviews of each product needs highlighting in product detail.
Improvement: Highlight user reviews more prominently on product pages. Introduce a rating system and allow users to filter reviews by rating or date. Encourage reviews by offering incentives.

Improved Error Messages and Feedback:
Current Issue: Error messages are often vague and unhelpful, leaving users frustrated.
Improvement: Provide clear and actionable error messages. Use user-friendly language and offer solutions or next steps when an error occurs.
