import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: "Meowcraft",
  tagline: "Školský projekt na predmet SMVIT",
  favicon: "img/favicon.ico",

  // Set the production url of your site here
  url: "https://johnnyjonky.github.io",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/meowcraft-smvit/",

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "johnnyjonky", // Usually your GitHub org/user name.
  projectName: "meowcraft-smvit", // Usually your repo name.
  trailingSlash: true,

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "sk-SK",
    locales: ["sk-SK"],
  },

  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: "./sidebars.ts",          
        },
        theme: {
          customCss: "./src/css/custom.css",
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: "img/docusaurus-social-card.jpg",
    navbar: {
      title: "Meowcraft",
      logo: {
        alt: "Meowcraft Logo",
        src: "img/logo-light.png",
        srcDark: "img/logo-dark.png",
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "tutorialSidebar",
          position: "left",
          label: "Dokumentácia",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Dokumenty",
          items: [
            {
              label: "Stojan v tvare mačky",
              to: "/docs/head-stand",
            },
            {
              label: "Stojan na sluchátka",
              to: "/docs/headphone-holder",
            },
            {
              label: "Multifunkčný stojan na Apple produkty",
              to: "/docs/multi-stand",
            },
            {
              label: "Tričká pre programátorov",
              to: "/docs/t-shirts",
            },
          ],
        },
        {
          title: "SMVIT Linky",
          items: [
            {
              label: "Bitbucket",
              href: "https://bitbucket.org/meowcraft_smvit/workspace/overview/",
            },
            {
              label: "Teams",
              href: "https://teams.microsoft.com/l/team/19%3A8pgw9Gb-cPBkmN_DfVOkbRchVIOBiMtYC0DiJuSfxUs1%40thread.tacv2/conversations?groupId=6123560a-4cbc-47c8-ae85-15490b49fafd&tenantId=25733538-6b16-4aa3-8ed6-297eb79b8e06",
            },
            {
              label: "Tabuľky",
              href: "https://stubask.sharepoint.com/sites/2024-2025-STHDF/_layouts/15/Doc.aspx?sourcedoc={85b1c11d-aaf1-40e1-a445-9772e797d64a}&action=view&wd=target%28_Collaboration%20Space%2F01.Teacher.one%7Cf508daab-eaf4-49fb-a4e3-d2790f96ea88%2FConditions%7C08aa3f73-fa17-0e46-850f-8f8847547686%2F%29&wdorigin=NavigationUrl",
            },
          ],
        },
        {
          title: "Sociálne siete",
          items: [
            {
              label: "YouTube",
              href: "https://www.youtube.com/@MeowCraft-Company",
            },
            {
              label: "LinkedIN",
              href: "https://www.linkedin.com/company/meowcraft/",
            },
            {
              label: "Patreon",
              href: "https://www.patreon.com/profile?u=145741883",
            },
          ],
        },
      ],
      copyright: `Vytvorené s ❤️ B. Hanusom, J. Hercegom, R. Matúšom a P. Serzodim  © ${new Date().getFullYear()} Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
