{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "def load_and_process(url_or_path_to_csv_file):\n",
    "    income = (\n",
    "        pd.read_csv(url_or_path_to_csv_file)\n",
    "        .set_axis(['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income'],axis=1,inplace=False)\n",
    "        .replace('?',np.nan)\n",
    "        .dropna()\n",
    "        .replace(\"?\",np.nan)\n",
    "        .dropna()\n",
    "    \n",
    ")\n",
    "    income2 = (\n",
    "        income\n",
    "        .drop(['fnlwgt','education-num','occupation','capital-gain','capital-loss'],axis=1)\n",
    ")\n",
    "\n",
    "    return income2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
