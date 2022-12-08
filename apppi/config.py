import os


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'fastjkdma;oiutrjf;wmgfoiewu4hjnlkhgierrioj'