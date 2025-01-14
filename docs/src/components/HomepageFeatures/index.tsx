import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Nabíjačky inšpirované mačkami',
    Svg: require('@site/static/img/cat_landing.svg').default,
    description: (
      <>
        V dokumentácii nájdeš návody na vymodelovanie a následné vytlačenie 3D modelov, pomocou ktorých si nabiješ svoje Apple zariadenia so štýlom. Priamo na tvojom stole
      </>
    ),
  },
  {
    title: 'Stojany na slúchadlá',
    Svg: require('@site/static/img/stand.svg').default,
    description: (
      <>
        Ak ti niekedy zavadzajú tvoje veľké slúchadlá na stole, v dokumentácii nájdeš návody na vytlačenie stojanov na slúchadlá, ktoré ti ušetria miesto a zároveň dodajú štýl tvojmu pracovnému stolu.
      </>
    ),
  },
  {
    title: 'Tričká pre programátorov',
    Svg: require('@site/static/img/solid.svg').default,
    description: (
      <>
        Každý programátor pozná úskalia rôznych povinností. Prinášame spôsob, ako si vyrobiť tričká s vtipnými nápismi, ktoré ti pomôžu vyjadriť svoje pocity pri každodennom živote programátora.
      </>
    ),
  },
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
