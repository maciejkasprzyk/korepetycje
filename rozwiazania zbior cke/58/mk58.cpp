#include <bits/stdc++.h>

using namespace std;

const int ROZM = 1095;
int g1[ROZM];
int g2[ROZM];
int g3[ROZM]; // godziny
int t1[ROZM], t2[ROZM], t3[ROZM]; // temperatury
ofstream out;

string zDziesietnego(int zamieniana, int podstawa)
{
  string wynik = "";
  bool ujemna = false;

  if (zamieniana < 0)
  {
    ujemna = true;
    zamieniana = -zamieniana;
  }

  // przypadek graniczny
  if (zamieniana == 0)
    return "0";

  while (zamieniana > 0)
  {
    char z = zamieniana % podstawa + '0' ;
    wynik = z + wynik;
    zamieniana /= podstawa; // zamieniana = zamieniania / podstawa
  }

  if (ujemna)
    wynik = '-' + wynik;

  return wynik;
}

// https://eduinf.waw.pl/inf/alg/006_bin/0003.php
// ladnie rozpisany schemat hornera ^
int naDziesietny(string zamieniana, int podstawa)
{
  int wynik = 0;

  bool czyUjemna = false;

  int i = 0;
  if (zamieniana[0] == '-')
  {
    czyUjemna = true;
    i++;
  }

  for (; i < zamieniana.length(); i++)
  {
    wynik = wynik * podstawa + (zamieniana[i] - '0');
  }

  if (czyUjemna)
  {
    return -wynik;
  }
  return wynik;
}

void zad1()
{
  int i;
  int min1 = t1[0], min2 = t2[0], min3 = t3[0];

  for (i = 1; i < ROZM; i++)
  {
    if (t1[i] < min1)
      min1 = t1[i];
    if (t2[i] < min2)
      min2 = t2[i];
    if (t3[i] < min3)
      min3 = t3[i];
  }
  out << "Zad 1: " << endl;
  out << "Min temp w stacji S1: " << zDziesietnego(min1, 2) << endl;
  out << "Min temp w stacji S2: " << zDziesietnego(min2, 2) << endl;
  out << "Min temp w stacji S3: " << zDziesietnego(min3, 2) << endl;
}

void zad2()
{
  int licznik = 0, oczekiwana = 12;

  for (int i = 0; i < ROZM; i++)
  {
    if (g1[i] != oczekiwana && g2[i] != oczekiwana && g3[i] != oczekiwana)
      licznik++;
    oczekiwana += 24;
  }

  out << "Zad 2: " << endl;
  out << "Liczba dni z blednymi zegarami: " << licznik << endl;
}

void zad3()
{
  int max1 = t1[0], max2 = t2[0], max3 = t3[0];
  int licz = 1;
  bool bylRekord;
  for (int i = 1; i < ROZM; i++)
  {
    bylRekord = false;
    if (t1[i] > max1)
    {
      max1 = t1[i];
      bylRekord = true;
    }
    if (t2[i] > max2)
    {
      max2 = t2[i];
      bylRekord = true;
    }
    if (t3[i] > max3)
    {
      max3 = t3[i];
      bylRekord = true;
    }
    if (bylRekord)
      licz++;
  }

  out << "Zad 3: " << endl;
  out << "Liczba rekordow: " << licz << endl;
}

void zad4()
{
  int skok;
  int maksSkok = 0;
  int rij;
  for (int i = 0; i < ROZM; i++)
    for (int j = i + 1; j < ROZM; j++)
    {
      rij = (t1[i] - t1[j]) * (t1[i] - t1[j]);

      skok = rij / (j - i);
      // zaokraglenie w górę
      if (skok * (j - i) < rij)
        skok++;

      if (skok > maksSkok)
      {
        maksSkok = skok;
      }
    }

  out << "Zad 4: " << endl;
  out << "Najwiekszy skok: " << maksSkok << endl;
}

int main()
{
  ifstream plik1, plik2, plik3;
  plik1.open("dane_systemy1.txt");
  plik2.open("dane_systemy2.txt");
  plik3.open("dane_systemy3.txt");

  string godzina, temperatura;
  for (int i = 0; i < ROZM; i++)
  {
    plik1 >> godzina >> temperatura;
    g1[i] = naDziesietny(godzina, 2);
    t1[i] = naDziesietny(temperatura, 2);

    plik2 >> godzina >> temperatura;
    g2[i] = naDziesietny(godzina, 4);
    t2[i] = naDziesietny(temperatura, 4);

    plik1 >> godzina >> temperatura;
    g3[i] = naDziesietny(godzina, 8);
    t3[i] = naDziesietny(temperatura, 8);
  }
  plik1.close();
  plik2.close();
  plik3.close();

  out.open("wynik.txt");
  zad1();
  zad2();
  zad3();
  zad4();

  out.close();

  return 0;
}