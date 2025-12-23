import random
gen_otps = set()   
num=int(input("Enter number of OTPs to generate: "))
for i in range(1, num+1):
    while True:
        otp = random.randint(1000, 9999)  
        if otp not in gen_otps:
            gen_otps.add(otp)
            print("Generated OTP:", otp)
            break

print("All OTPs:", list(gen_otps))