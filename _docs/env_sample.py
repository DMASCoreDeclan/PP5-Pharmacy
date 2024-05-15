import os

os.environ.setdefault( "SECRET_KEY", "someStringVariable")
os.environ.setdefault( "DEVELOPMENT", "1") # Allows DEBU = True on Heroku
os.environ.setdefault( "STRIPE_PUBLIC_KEY", "someStringVariable") # Stripe Test Keys
os.environ.setdefault( "STRIPE_SECRET_KEY", "someStringVariable") # Stripe Test Keys
os.environ.setdefault( "STRIPE_PUBLIC_KEY", "someStringVariable") # Stripe Live Keys
os.environ.setdefault( "STRIPE_SECRET_KEY", "someStringVariable") # Stripe Live Keys
os.environ.setdefault( "STRIPE_WH_SECRET", "whsec_4doHZbBbuBpPHkXrYucAU23URA67QwjH") # Stripe Live Keys
os.environ.setdefault( "EMAIL_HOST_PASS", "SomeStringVariable") # Email passwrod
os.environ.setdefault( "EMAIL_HOST_USER", "SomeStringVariable@gmail.com") # Email adress
os.environ.setdefault( "AWS_STORAGE_BUCKET_NAME", "SomeStringVariable")
os.environ.setdefault( "AWS_S3_REGION_NAME", "SomeStringVariable")
os.environ.setdefault( "AWS_S3_CUSTOM_DOMAIN", 'aws_storage_bucket_name_from_above.s3.amazonaws.com')
