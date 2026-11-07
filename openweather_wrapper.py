#!/usr/bin/env python3
"""Python wrapper for OpenWeatherMap API"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Python wrapper for OpenWeatherMap API")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("openweather-wrapper v0.1.0");return
 print(f"[12:01] openweather-wrapper ready")
if __name__=="__main__":main()
