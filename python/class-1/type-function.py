>>> type(1)     # টাইপ ফাংশনের প্যারামিটার হিসেবে ইন্টেজার 1 পাস করা হল
<class 'int'>   # ফাংশনটি ১ এর টাইপ রিটার্ন করল, <class 'int'> এখানে 'int' মানে হল ইন্টেজার (integer) নাম্বের

>>> type(2.2)   # ফ্লোট নাম্বার পাস করলে টাইপ হিসেবে 
<class 'float'> # ফ্লোট (float) ই দেখাবে

>>> type("Hello World")  # স্ট্রিং কেও স্ট্রিং হিসেবেই দেখানো উচিত
<class 'str'>            # এবং তাই দেখিয়েছে, 'str' দিয়ে 'string' বোঝানো হয়েছে

>>> type("3")  # এটা কি ইন্টেজার!? নাকি স্ট্রিং !? 
<class 'str'>  # স্ট্রিং, কেন? কারন এটা কোটেশনের ভিতর রয়েছে !! 

>>> type('2.3') # কোটেশনের ভিতর থাকলেই স্ট্রিং... যাই থাকুক না কেন! 
<class 'str'>   # এমনকি ফ্লোটিং নাম্বার থাকলেও তা স্ট্রিং! 

>>> type(True)  # বুলিয়ান ভ্যালুর টাইপ কি হতে পারে ?
<class 'bool'>  # অবশ্যই বুলিয়ান!

>>> type('True') # জয়, স্ট্রিং এর জয়... 
<class 'str'>   # !!!
