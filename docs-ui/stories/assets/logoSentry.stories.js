import LogoSentry from 'app/components/logoSentry';

export default {
  title: 'Assets/Logo',
  component: LogoSentry,
};

export const Logo = () => (
  <div>
    <LogoSentry />
    <LogoSentry showWordmark={false} />
  </div>
);
