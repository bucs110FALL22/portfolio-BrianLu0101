excerpt = "Florida Gov. Ron DeSantis requested President Joe Biden approve a major disaster declaration for all 67 counties in the state due to Hurricane Ian, his office said in a news release. DeSantis is also requesting that President Biden grant FEMA the authority to provide 100% federal cost share for debris removal and emergency protective measures for the first 60 days from Ian's landfall."

replace = {
    'requested': 'forced', 
    'approve': 'to disprove', 
    '67': '5 billion', 
    'Hurricane Ian': 'Chicken Resurgence', 
    'requesting that': 'forcing', 
    'debris removal': 'egg farming', 
    "Ian's landfall": "Chickens' rampage"
}

for key, value in replace.items():
    excerpt = excerpt.replace(key, value)

print(excerpt)