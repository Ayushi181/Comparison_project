from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def scrape_amazon():
    # Make a GET request to the Amazon product page
    url = "https://www.amazon.in/realme-Feather-Segment-Charging-Slimmest/dp/B0C45N5VPT?pf_rd_r=HP90PZVKY6N6PMZTSP7F&pf_rd_t=PageFrameworkApplication&pf_rd_i=1389401031&pf_rd_p=111bee0e-b3d7-4d51-89e6-66e252d98c6c&pf_rd_s=merchandised-search-2&ref=dlx_13894_sh_dcl_img_0_6ef29c09_dt_mese2_6c"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the technical details section on the page
    technical_details_div = soup.find(id="technicalSpecifications_feature_div")

    # Extract the text of the technical details
    technical_details = technical_details_div.get_text(strip=True)

    return render_template('index.html', technical_details=technical_details)

if __name__ == '__main__':
    app.run(debug=True)
