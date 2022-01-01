<div id="top"></div>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO
<br />
<div align="center">
  <a href="https://github.com/richmoolah/microprojects">
    <img src="misc/fish.jpg" alt="Logo" width="80" height="80">
  </a>
-->


<h3 align="center">microprojects</h3>

  <p align="center">
    an interactive maze and animated visualization of computer pathfinding using matplotlib that can be configured for Dijkstra's, BFS, and DFS etc.
    <br />
    <a href="https://github.com/richmoolah/microprojects"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/richmoolah/microprojects">View Demo</a>
    ·
    <a href="https://github.com/richmoolah/microprojects/issues">Report Bug</a>
    ·
    <a href="https://github.com/richmoolah/microprojects/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](misc/grid-crawler.gif)

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With



* [python3](https://www.python.org/)
* [matplotlib](https://matplotlib.org/)
* [numpy](https://numpy.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Install python3
   ```sh
   sudo apt-get update
   sudo apt-get install python3
   ```   

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/richmoolah/microprojects.git
   ```

2. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```

3. Run stuckfish.py
    ```sh
    python3 /grid-crawler/stuckfish.py
    ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Grid-crawler is a simple application that visualizes common computer pathfinding algorithms using an interative grid and animation. The application was originally configured for DFS and BFS, but in its current state mimics Dijkstra's search pattern in code. However, because distances between squares is all equal, the search pattern visually more closely resembles BFS.

The start and end points are randomly selected.

Click once to set an obstacle between the two points. Click that cell again to remove the obstacle.

Press space to begin the search algorithm.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] DFS/BFS
- [x] Dijkstra
- [ ] A*
- [ ] Support for input of edge weights

See the [open issues](https://github.com/richmoolah/microprojects/issues) for tracked issues.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Currently microprojects is a personal project used for learning but if you would like to contribute to it, please reach out at the contact below!

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Richard Xu - richardxu@uchicago.edu

Project Link: [https://github.com/richmoolah/microprojects](https://github.com/richmoolah/microprojects)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Thanks to CLRS for providing the algorithm for Dijkstra's, BFS, and DFS.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/richmoolah/microprojects.svg?style=for-the-badge
[contributors-url]: https://github.com/richmoolah/microprojects/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/richmoolah/microprojects.svg?style=for-the-badge
[forks-url]: https://github.com/richmoolah/microprojects/network/members
[stars-shield]: https://img.shields.io/github/stars/richmoolah/microprojects.svg?style=for-the-badge
[stars-url]: https://github.com/richmoolah/microprojects/stargazers
[issues-shield]: https://img.shields.io/github/issues/richmoolah/microprojects.svg?style=for-the-badge
[issues-url]: https://github.com/richmoolah/microprojects/issues
[license-shield]: https://img.shields.io/github/license/richmoolah/microprojects.svg?style=for-the-badge
[license-url]: https://github.com/richmoolah/microprojects/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/richardxu5
[product-screenshot]: misc/grid-crawler.gif
