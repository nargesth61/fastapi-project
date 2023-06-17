import random 
import uuid
from fastapi import APIRouter, HTTPException
from schemas import CreateOTP
from utils import emailutils
from enum import Enum


class OTPType(str, Enum):
    phone = "Phone"
    email = "Email"

def otp_code():
    otp =random.randint(1000,9999)
    return otp

router = APIRouter(refix='/api/v1')


