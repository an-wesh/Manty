import { useSession, signIn, signOut } from 'next-auth/react';
import { User } from '@/types';

export function useAuth() {
  const { data: session, status } = useSession();

  const user: User | null = session?.user ? {
    id: session.user.id,
    email: session.user.email || '',
    name: session.user.name || undefined,
    image: session.user.image || undefined,
    createdAt: new Date(),
    updatedAt: new Date(),
  } : null;

  return {
    user,
    isLoading: status === 'loading',
    isAuthenticated: status === 'authenticated',
    signIn,
    signOut,
  };
}