from brownie import Dogger, accounts

def main():
    compte = accounts.load('crazydog')
    t = Dogger.deploy({'from': compte})
