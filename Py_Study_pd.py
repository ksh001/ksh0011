{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPcEJNSaqE7VZ0zCa7NFr4t",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ksh001/ksh0011/blob/main/Py_Study_pd.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eJUZ9A-18sEA"
      },
      "source": [
        "Pandas study 20.12.31."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MzqXYAAD_SPl"
      },
      "source": [
        "import pandas as pd"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iVg85Fie87gi"
      },
      "source": [
        "df = pd.DataFrame(\r\n",
        "  {\"a\" : [4 ,5, 6],\r\n",
        "  \"b\" : [7, 8, 9],\r\n",
        "  \"c\" : [10, 11, 12]},\r\n",
        "index = [1, 2, 3])"
      ],
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        },
        "id": "SjCPPsUC_7FI",
        "outputId": "f51b535b-f08c-4f79-b863-4eceb010841e"
      },
      "source": [
        "df"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>7</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   a  b   c\n",
              "1  4  7  10\n",
              "2  5  8  11\n",
              "3  6  9  12"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        },
        "id": "Zb_PCy06AlP1",
        "outputId": "13ff6eb4-34e6-424a-ed19-7243f7473fd5"
      },
      "source": [
        "df = pd.DataFrame( #low\r\n",
        "  [[4, 7, 10],\r\n",
        "  [5, 8, 11], \r\n",
        "  [6, 9, 12]],\r\n",
        "  index=[1, 2, 3],\r\n",
        "  columns=['a', 'b', 'c']) #colums\r\n",
        "df"
      ],
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>7</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   a  b   c\n",
              "1  4  7  10\n",
              "2  5  8  11\n",
              "3  6  9  12"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gxf7tjgjCocy",
        "outputId": "e3114bf9-1761-491b-901c-89234aaf6780"
      },
      "source": [
        "df.loc[2]"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "a     5\n",
              "b     8\n",
              "c    11\n",
              "Name: 2, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "pylQ_NeqECJD",
        "outputId": "a604c903-7e8b-4cb7-b2de-ae46a3ab69cd"
      },
      "source": [
        "df.loc[[1, 2], ['a', 'b'] ]"
      ],
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>7</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   a  b\n",
              "1  4  7\n",
              "2  5  8"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3cdqDWOyFIJW",
        "outputId": "ade8e139-448d-4b78-83dd-6fe563098ef1"
      },
      "source": [
        "df.a > 5"
      ],
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1    False\n",
              "2    False\n",
              "3     True\n",
              "Name: a, dtype: bool"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "kC3yEbk6FS8e",
        "outputId": "4e5ac43a-fdb4-40a2-9f56-11212541c7e7"
      },
      "source": [
        "df[df.a > 4] #a열을 기준으로 True인 행을 모두 가져오겠다."
      ],
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   a  b   c\n",
              "2  5  8  11\n",
              "3  6  9  12"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 49
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 195
        },
        "id": "mGP7qP_mAzLn",
        "outputId": "e026f679-6177-43ff-9a9f-2be0262d2d55"
      },
      "source": [
        "df = pd.DataFrame(\r\n",
        "  {\"apple\" : [4 ,5, 6, 6],\r\n",
        "  \"bee\" : [7, 8, 9, 9],\r\n",
        "  \"cat\" : [10, 11, 12, 12]},\r\n",
        "index = pd.MultiIndex.from_tuples(\r\n",
        "  [('d',1),('d',2),('e',1), ('e',2)],\r\n",
        "  names=['n','v']))\r\n",
        "\r\n",
        "df"
      ],
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">d</th>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>7</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">e</th>\n",
              "      <th>1</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     a  b   c\n",
              "n v          \n",
              "d 1  4  7  10\n",
              "  2  5  8  11\n",
              "e 1  6  9  12\n",
              "  2  6  9  12"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 54
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Txfq3EktCEk4",
        "outputId": "ca81a58f-bb56-4194-eedb-1a6b39f778e5"
      },
      "source": [
        "df['a']"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "n  v\n",
              "d  1    4\n",
              "   2    5\n",
              "e  2    6\n",
              "Name: a, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2OFFHUnLCFma",
        "outputId": "8cabc45e-da5a-4dc1-b0c8-6aabc44f8e1e"
      },
      "source": [
        "df.a"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "n  v\n",
              "d  1    4\n",
              "   2    5\n",
              "e  2    6\n",
              "Name: a, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oAF6-Ae0CWqM",
        "outputId": "165574ee-3eff-473d-f377-39e05de71d04"
      },
      "source": [
        "df.loc[('d',2)]"
      ],
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "a     5\n",
              "b     8\n",
              "c    11\n",
              "Name: (d, 2), dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6nsk1pXgCZPw",
        "outputId": "2ca0e7bf-a525-4c48-9051-56f6a76ce568"
      },
      "source": [
        "df.loc[('e',2), 'c']"
      ],
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "12"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        },
        "id": "Zk1e6AlrDc_m",
        "outputId": "3d77fd78-3ab3-4915-b7d4-6716f5acc636"
      },
      "source": [
        "df.loc[[('d', 1), ('e', 2)], ['a', 'b', 'c']]"
      ],
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>d</th>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>7</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>e</th>\n",
              "      <th>2</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     a  b   c\n",
              "n v          \n",
              "d 1  4  7  10\n",
              "e 2  6  9  12"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 195
        },
        "id": "m68nszN7G-y-",
        "outputId": "3fb8b796-d25e-4fc9-8b2f-259468523140"
      },
      "source": [
        "df"
      ],
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">d</th>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>7</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">e</th>\n",
              "      <th>1</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     a  b   c\n",
              "n v          \n",
              "d 1  4  7  10\n",
              "  2  5  8  11\n",
              "e 1  6  9  12\n",
              "  2  6  9  12"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 55
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 166
        },
        "id": "EPd5GhLGEtxl",
        "outputId": "5d03b9cd-8dec-4470-d622-f061a2220962"
      },
      "source": [
        "df.drop_duplicates() #중복되는 열 제거 _ 아예 지우는 게 아니라 출력만 / df에 대입하면 제거됨"
      ],
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">d</th>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>7</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>e</th>\n",
              "      <th>1</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     a  b   c\n",
              "n v          \n",
              "d 1  4  7  10\n",
              "  2  5  8  11\n",
              "e 1  6  9  12"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 56
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        },
        "id": "WSQQThZNHxOK",
        "outputId": "5497d1c7-ed95-441e-d322-f899ffa70211"
      },
      "source": [
        "df.head(2)#위에서부터 2개의 행 가져오기"
      ],
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">d</th>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>7</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     a  b   c\n",
              "n v          \n",
              "d 1  4  7  10\n",
              "  2  5  8  11"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "K4gCpur8H-RF",
        "outputId": "9fb44b2a-ffa2-4299-fdfe-7e94e73364b5"
      },
      "source": [
        "df.tail(1) #뒤에서 1개 가져오기"
      ],
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>e</th>\n",
              "      <th>2</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     a  b   c\n",
              "n v          \n",
              "e 2  6  9  12"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 58
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        },
        "id": "7hzuAQnEIbWt",
        "outputId": "9cdfbd6e-cebe-4520-862c-82f2dba3df80"
      },
      "source": [
        "df.sample(frac=0.6) # 더 가까운 곳으로 뜬다"
      ],
      "execution_count": 72,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">d</th>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>7</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     a  b   c\n",
              "n v          \n",
              "d 2  5  8  11\n",
              "  1  4  7  10"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 72
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 166
        },
        "id": "hyzQegHhJfgN",
        "outputId": "fa88489d-c44d-4f75-bf30-25ed63c009ca"
      },
      "source": [
        "df.iloc[0: 3]  #  배열의 index처럼 시작점과 끝지점으로부터 한 칸 더(이터레이터?) : [시작위치, 끝 위치 + 1]"
      ],
      "execution_count": 81,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">d</th>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>7</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>e</th>\n",
              "      <th>1</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     a  b   c\n",
              "n v          \n",
              "d 1  4  7  10\n",
              "  2  5  8  11\n",
              "e 1  6  9  12"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 81
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 166
        },
        "id": "mtcvbXMGLM_a",
        "outputId": "5871fc84-202c-4f25-a5dd-c2ff5e827f83"
      },
      "source": [
        "df.nlargest(3, 'a') # df.nlargest(n, 'value') : 'b'열에서 제일 큰 값 순서로 3개"
      ],
      "execution_count": 95,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">e</th>\n",
              "      <th>1</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>d</th>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     a  b   c\n",
              "n v          \n",
              "e 1  6  9  12\n",
              "  2  6  9  12\n",
              "d 2  5  8  11"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 95
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        },
        "id": "4IU7XqTaMH8b",
        "outputId": "27247fa8-4d09-47ca-9f64-9bb2343a9801"
      },
      "source": [
        "df.nsmallest(2, 'a')"
      ],
      "execution_count": 96,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">d</th>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>7</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     a  b   c\n",
              "n v          \n",
              "d 1  4  7  10\n",
              "  2  5  8  11"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 96
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 195
        },
        "id": "uAAr1L3YMO-9",
        "outputId": "b4f38a0a-62bc-4cd3-d30a-7fdc763b3aff"
      },
      "source": [
        "df[['a', 'c']]"
      ],
      "execution_count": 98,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">d</th>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">e</th>\n",
              "      <th>1</th>\n",
              "      <td>6</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>6</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     a   c\n",
              "n v       \n",
              "d 1  4  10\n",
              "  2  5  11\n",
              "e 1  6  12\n",
              "  2  6  12"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 98
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 195
        },
        "id": "KqLjSpPKMsNK",
        "outputId": "a9ce08ea-6416-48ec-96eb-342b2964f73e"
      },
      "source": [
        "df"
      ],
      "execution_count": 100,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">d</th>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>7</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">e</th>\n",
              "      <th>1</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>6</td>\n",
              "      <td>9</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     a  b   c\n",
              "n v          \n",
              "d 1  4  7  10\n",
              "  2  5  8  11\n",
              "e 1  6  9  12\n",
              "  2  6  9  12"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 100
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 195
        },
        "id": "fR9sRCMTMW92",
        "outputId": "b97167bf-3ea6-401a-bc17-8a45251a565d"
      },
      "source": [
        "df.filter(regex='^a') #a로 시작하는 것만 뜸"
      ],
      "execution_count": 103,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">d</th>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">e</th>\n",
              "      <th>1</th>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     a\n",
              "n v   \n",
              "d 1  4\n",
              "  2  5\n",
              "e 1  6\n",
              "  2  6"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 103
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 179
        },
        "id": "Hh0yLDeqNaGy",
        "outputId": "ee129384-5e54-4586-bca3-241750d5ec22"
      },
      "source": [
        "df.filter(regex='e$') #e로 끝나는 것만 뜸"
      ],
      "execution_count": 104,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>n</th>\n",
              "      <th>v</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">d</th>\n",
              "      <th>1</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th rowspan=\"2\" valign=\"top\">e</th>\n",
              "      <th>1</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "Empty DataFrame\n",
              "Columns: []\n",
              "Index: [(d, 1), (d, 2), (e, 1), (e, 2)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 104
        }
      ]
    }
  ]
}