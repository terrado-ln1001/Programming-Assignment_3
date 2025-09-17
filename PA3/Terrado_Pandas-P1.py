{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "53d7d745-f070-403c-87c9-b73d744252de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  \\\n",
      "0           Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1   \n",
      "1       Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1   \n",
      "2          Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1   \n",
      "3      Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0   \n",
      "4   Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0   \n",
      "27       Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.90   1   1   \n",
      "28     Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.50   0   1   \n",
      "29       Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.50   0   1   \n",
      "30      Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.60   0   1   \n",
      "31         Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.60   1   1   \n",
      "\n",
      "    gear  carb  \n",
      "0      4     4  \n",
      "1      4     4  \n",
      "2      4     1  \n",
      "3      3     1  \n",
      "4      3     2  \n",
      "27     5     2  \n",
      "28     5     4  \n",
      "29     5     6  \n",
      "30     5     8  \n",
      "31     4     2  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "cars = pd.read_csv(\"cars.csv\")\n",
    "result = pd.concat([cars.head(5), cars.tail(5)])\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a41898f3-0482-48fe-9d62-05c556c362cd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
