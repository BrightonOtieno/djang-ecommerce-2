# STORE THE 
# will be stored in user profile model

# MODEL

"""
# PROFILE MODEL
class UserProfileI(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE)
    stripe_customer_id = models.CharField( max_length=50,blank=True,null=True)
    one_click_purchasing = models.BooleanField()
    

    def __str__(self):
        return self.user.username
    
# POST SAVE SIGNAL
# post save_signal will create profile for a user immediately the user is created
def userprofile_receiver(sender,instance,created,*args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver,sender=User)



"""



# VIEW
# PAYMENT 
def post(self,*args,**kwargs):


    # a lot of stuff




    if form.is_valid():
        token
        save #-> true or false value from form  (save for latter use)  from cleaned_data
        use_default # if user selected (use_card as default ) from cleaned_data

        if save:
            # if they don't have a stripe_customer_id:
            # send their purchase info to stripe so we can get an id from stripe
            if not userprofile.stripe_customer_id:
                customer = stripe.Customer.create(
                    email = self.request.user.email,
                    source = token
                )

                #save the id to the users profile
                userprofile.stripe_customer_id = customer['id']
                userprofile.one_click_purchasing = True
                userprofile.save()

            # if they have a stripe_customer_id -> there info is in there profile
            # send a details of user to stripe so that it can fetch the CARD
            else:
                stripe.Customer.create_source(
                    userprofile.stripe_customer_id,
                    source = token
                )
        amount #------------


        try:
            # NOW WANT TO CHARGE THE USER  
            # check if they allowed for use of default card
            if use_default:
                charge = stripe.Charge.create(
                    amount
                    currency
                    customer = userprofile.stripe_customer_id

                )
            # if they they didn't allow for use of default card    
            else:
                charge = stripe.Charge.create(
                    amount
                    currency
                    source = token
                )
            
            payment = Payment()
            #------




def get(------------):
    # grab user profile 
    # check if one_click_purchasing is enabled
    # meaning they have (SAVE FOR LATER)

    userprofile = self.request.user.userprofile
    if userprofile.one_click_purchasing:
        # fetch the users LIST OF CARDS
        cards = stripe.Customer.list_source(
            #pass in their id 
            userprofile.stripe_customer_id ,
            limit = 3, #-> how many cards
            object = 'card' # what do you want to get (cards)

        )
        card_list = cards['data']
        if len(card_list) > 0:

            # grab the first card 
            #and update the context with that card
            context = {
                'card':card_list
            }
    return render------




    # TEMPLATE 
    {% if card %}
                {{card.last4}}
                {{card.exp_month}} {{card.exp_year}}

